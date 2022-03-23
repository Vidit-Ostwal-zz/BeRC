from collections import defaultdict
from typing import Dict, Tuple

import librosa as lr
import numpy as np
import torchaudio
from jina import Executor, DocumentArray, requests, Document
from jina.excepts import BadRequestType


class AudioSegmenter(Executor):
    """
    ``AudioTimeSegmenter`` segments audio signals based on fixed time intervals.
    For each document, the ``AudioTimeSegmenter`` first converts the document content into
    a 1D tensor, tagged with a ``sample_rate`` if the input is not already a tensor
    (i.e. an uri).
    Then, the ``AudioTimeSegmenter`` converts the ``interval`` and ``stride`` provided in
    ``parameters`` measured in seconds to their sizes relative to the length of
    the array (i.e. ``window_size and ``stride_size``), using the given ``sample_rate`` in
    document's tag. If ``interval`` and ``stride`` are not provided, then ``default_interval``
    and ``default_stride`` provided at initialization are used instead.
    After that, starting at index 0, the next ``window_size`` elements in the array are taken
    as the first chunk. We then move ``stride_size`` elements forward along the signal array,
    take the next ``window_size`` elements as the next chunk. We repeat this ``num_chunks``
    of times. Thus, we should expect all chunks to have ``window_size``.
    If audio signal has a time length less than the specified interval, then no chunk
    will be appended to the document.
    """

    def __init__(
        self,
        default_interval: int = 10,
        default_stride: int = 1,
        default_traversal_paths: str = '@r',
        *args,
        **kwargs
    ):
        """
        :param default_interval: the default length of the time interval for each chunk
        to be segmented in seconds
        :param default_stride: the default stride length in seconds
        """
        super().__init__(*args, **kwargs)
        self.default_interval = default_interval
        self.default_stride = default_stride
        self.default_traversal_paths = default_traversal_paths

    @requests(on=['/search', '/index'])
    def segment(self, docs: DocumentArray, parameters: Dict, **kwargs):
        """
        :param docs: the input ``DocumentArray`` with either: 1. an ``uri`` containing the path
        to the audio signal or; 2. a 1D ``tensor`` representing the audio signal, with
        ``sample_rate`` of the signal specified in ``doc.tags``
        :param parameters: The ``interval`` and ``stride`` parameters, where ``interval`` is the
        max time interval of each chunk measured in seconds, ``stride`` is the time length to
        stride forward to take the next chunk (also measured in seconds).
        """

        if not docs:
            return

        interval = parameters.get('interval', self.default_interval)
        stride = parameters.get('stride', self.default_stride)
        traversal_paths = parameters.get(
            'traversal_paths', self.default_traversal_paths
        )

        for idx, doc in enumerate(docs[traversal_paths]):
            doc.tensor, sample_rate = self._load_raw_audio(doc)
            window_size = int(interval * sample_rate)
            stride_size = int(stride * sample_rate)
            doc.tags['sample_rate'] = sample_rate

            # calculate output size (i.e. num_chunks)  based on the formula:
            # output_size = [(input_size - window_size) / stride_size] + 1
            num_chunks = max(
                0, int((doc.tensor.shape[0] - window_size) / stride_size) + 1
            )

            for chunk_id in range(num_chunks):
                beg = chunk_id * stride_size
                end = beg + window_size
                doc.chunks.append(
                    Document(
                        tensor=doc.tensor[beg:end],
                        offset=idx,
                        location=[beg, end],
                        tags=doc.tags,
                    )
                )

    def _load_raw_audio(self, doc: Document) -> Tuple[np.ndarray, int]:
        if doc.tensor is not None and doc.tags.get('sample_rate', None) is None:
            raise BadRequestType('data is tensor but sample rate is not provided')
        elif doc.tensor is not None:
            return doc.tensor, int(doc.tags['sample_rate'])
        elif doc.uri is not None and doc.uri.endswith('.mp3'):
            return self._read_mp3(doc.uri)
        elif doc.uri is not None and doc.uri.endswith('.wav'):
            return self._read_wav(doc.uri)
        else:
            raise BadRequestType('doc needs to have either a tensor or a wav/mp3 uri')

    def _read_wav(self, file_path: str) -> Tuple[np.ndarray, int]:
        data, sample_rate = torchaudio.load(file_path)
        data = np.mean(data.cpu().numpy(), axis=0)
        return data, sample_rate

    def _read_mp3(self, file_path: str) -> Tuple[np.ndarray, int]:
        return lr.load(file_path)

class MyRanker(Executor):
    @requests(on="/search")
    def rank(self, docs: DocumentArray = None, **kwargs):
        for doc in docs["@r"]:
            parents_scores = defaultdict(list)
            parents_match = defaultdict(list)
            for m in DocumentArray([doc])["@cm"]:
                parents_scores[m.parent_id].append(m.scores["cosine"].value)
                parents_match[m.parent_id].append(m)
            # Aggregate match scores for parent document and
            # create doc's match based on parent document of matched chunks
            new_matches = []
            for match_parent_id, scores in parents_scores.items():
                score_id = np.argmin(scores)
                score = scores[score_id]
                match = parents_match[match_parent_id][score_id]
                new_match = Document(
                    uri=match.uri, id=match_parent_id, scores={"cosine": score}
                )
                new_match.tags["beg_in_ms"] = match.tags["beg_in_ms"]
                new_match.tags["end_in_ms"] = match.tags["end_in_ms"]
                new_matches.append(new_match)
            # Sort the matches
            doc.matches = new_matches
            doc.matches = DocumentArray(sorted(doc.matches, key=lambda d: d.scores[
                "cosine"].value))
