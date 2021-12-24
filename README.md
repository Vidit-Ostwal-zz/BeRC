# Beat Recommender
Ever liked a particular beat, but struggled to find similar beats,<br>
Well we have a solution for this,<br>
Introducing beat recommender build with JINA 

# DataSet Used
- The dataset includes ~9.5k samples unequally distributed among 41 categories. The minimum number of audio samples per category in the train set is 94, and the maximum 300. The duration of the audio samples ranges from 300ms to 30s due to the diversity of the sound categories and the preferences of Freesound users when recording sounds. The total duration of the train set is roughly 18h.

- Out of the ~9.5k samples from the train set, ~3.7k have manually-verified ground truth annotations and ~5.8k have non-verified annotations. The non-verified annotations of the train set have a quality estimate of at least 65-70% in each category. Checkout the Data labeling process section below for more information about this aspect.

- All audio samples in this dataset are gathered from [Freesound](https://freesound.org/) and are provided here as uncompressed PCM 16 bit, 44.1 kHz, mono audio files. Note that because Freesound content is collaboratively contributed, recording quality and techniques can vary widely

- More information can be found [here](https://zenodo.org/record/2552860#.XFD05fwo-V4)
