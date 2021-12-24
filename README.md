

https://user-images.githubusercontent.com/65944284/147368602-a26839da-a62b-4afc-bc70-5f483d290680.mp4





# Beat Recommender

Introducing to you beat recommender build with [**JINA**](https://docs.jina.ai/) <br>
With over **9.5k+ beats embedded**, it hold one stop solution for beat recommendation.
<br>
<br>

# What is JINA ?
<p align="center">
<!--startmsg-->

<!--endmsg-->
</p>
<p align="center">
<a href="https://docs.jina.ai"><img src="https://github.com/jina-ai/jina/blob/master/.github/logo-only.gif?raw=true" alt="Jina logo: Jina is a cloud-native neural search framework" width="200px"></a>
</p>

<p align="center">
<b>Cloud-Native Neural Search<sup><a href="https://docs.jina.ai/get-started/neural-search/">?</a></sup> Framework for <i>Any</i> Kind of Data</b>
</p>


<p align=center>
<a href="https://pypi.org/project/jina/"><img src="https://github.com/jina-ai/jina/blob/master/.github/badges/python-badge.svg?raw=true" alt="Python 3.7 3.8 3.9" title="Jina supports Python 3.7 and above"></a>
<a href="https://pypi.org/project/jina/"><img src="https://img.shields.io/pypi/v/jina?color=%23099cec&amp;label=PyPI&amp;logo=pypi&amp;logoColor=white" alt="PyPI"></a>
<a href="https://hub.docker.com/r/jinaai/jina/tags"><img src="https://img.shields.io/docker/v/jinaai/jina?color=%23099cec&amp;label=Docker&amp;logo=docker&amp;logoColor=white&amp;sort=semver" alt="Docker Image Version (latest semver)"></a>
<a href="https://codecov.io/gh/jina-ai/jina"><img src="https://codecov.io/gh/jina-ai/jina/branch/master/graph/badge.svg" alt="codecov"></a>
<a href="https://slack.jina.ai"><img src="https://img.shields.io/badge/Slack-2.2k%2B-blueviolet?logo=slack&amp;logoColor=white"></a>
</p>

<!-- start elevator-pitch -->

Jina is a neural search framework that empowers anyone to build SOTA and scalable deep learning search applications in minutes.

⏱️ **Save time** - *The* design pattern of neural search systems. Native support for PyTorch/Keras/ONNX/Paddle. Build solutions in just minutes.

🌌 **All data types** - Process, index, query, and understand videos, images, long/short text, audio, source code, PDFs, etc.

🌩️ **Local & cloud friendly** - Distributed architecture, scalable & cloud-native from day one. Same developer experience on both local and cloud. 

🍱 **Own your stack** - Keep end-to-end stack ownership of your solution. Avoid integration pitfalls you get with
fragmented, multi-vendor, generic legacy tools.

More Information can be find [here](https://docs.jina.ai/)
<!-- end elevator-pitch -->

<br>
<br>

# DataSet Used
- The dataset includes ~9.5k samples unequally distributed among 41 categories. The minimum number of audio samples per category in the train set is 94, and the maximum 300. The duration of the audio samples ranges from 300ms to 30s due to the diversity of the sound categories and the preferences of Freesound users when recording sounds. The total duration of the train set is roughly 18h.

- Out of the ~9.5k samples from the train set, ~3.7k have manually-verified ground truth annotations and ~5.8k have non-verified annotations. The non-verified annotations of the train set have a quality estimate of at least 65-70% in each category. Checkout the Data labeling process section below for more information about this aspect.

- All audio samples in this dataset are gathered from [Freesound](https://freesound.org/) and are provided here as uncompressed PCM 16 bit, 44.1 kHz, mono audio files. Note that because Freesound content is collaboratively contributed, recording quality and techniques can vary widely

- More information can be found [here](https://zenodo.org/record/2552860#.XFD05fwo-V4)
