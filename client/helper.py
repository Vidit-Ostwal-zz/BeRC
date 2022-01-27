import os
import requests

class UI:
    about_block = """
    ### About
    This is a beat search engine using Jina's neural search framework [GitHub Repo](https://github.com/jina-ai/jina/)
    - GitHub Repo of the [project](https://github.com/Vidit-Ostwal/BeatRecommender)
    - Dataset [link](https://drive.google.com/drive/folders/1n8Ec9y1jZZc0qBAhwf6lYwjlEtn4NmSi?usp=sharing)
    """

    css = f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 1200px;
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }}
    .reportview-container .main {{
        color: "#111";
        background-color: "#eee";
    }}
</style>
"""


headers = {"Content-Type": "application/json"}

def get_matches(bytes_data):
    with open("audio.wav","wb") as f:
        f.write(bytes_data)
        
    PORT = 45678
    ENDPOINT = "/search"
    
    url = f"http://0.0.0.0:{PORT}{ENDPOINT}"
    headers = {"Content-Type":"application/json"}
    
    path = os.path.abspath("audio.wav")
    data = {"data":[{"uri" : path}]}
    
    try:
        response = requests.post(url,headers = headers,json = data)
        content = response.json()
        os.remove("audio.wav")
        return content["data"]["docs"][0]["matches"]
    except Exception:
        return []