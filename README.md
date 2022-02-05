# BeRC
BeRC (Beat Recommender) - Using this project one can enter any beat and search similar beats! The project is make using Jina AI which is a neural search engine.

## Idea:
Create a search hinge for beats using Jina

## What it does?
Upload an beat-audio and get similar beats like it.

## Tech stack used?
- Backend: Jina
- Frontend: Streamlit
- Dataset: [FreeSound Dataset](https://freesound.org/)

Made with ❤️

## How to use?
- Download the AudioCLIP model by running:

```
bash scripts/download_models.sh
```

Create a virtual environment

```
python3 -m venv berc-venv
```

Activate the virtual environment

```
source berc-venv/bin/activate
```

- Run the backend:

```
python3 app.py
```

- In another terminal, run streamlit:

```
streamlit run client/app.py
```

Now, head over to `http://localhost:8501` and you can query any beat of your choice!
