# Microservice for Python YtMusicApi

Microservice (tiny server) for [ytmusicapi](https://github.com/sigma67/ytmusicapi) compatible-ish with Youtube Data API v3.

## Important Notes

'ytmusicapi' is an unofficial tool to search for Youtube Music content. It can break anytime if Google decides to change anything regarding Youtube Music. As far as I know this is currently the only option to search Youtube Music since there is no official Google API :-/.  
**Use this only for private experiments!**

## Installation

- Install Python 3.6 or higher with Pip (tested on 3.9.2)
- Clone this repository: `git clone https://github.com/fquirin/python-ytmusicapi-server.git`
- Set up a virtual environment (recommended) and install packages:
```
cd python-ytmusicapi-server
python -m venv env && source env/bin/activate
pip install --upgrade pip
pip install fastapi
pip install uvicorn
pip install ytmusicapi
```

## Run the Server

- `uvicorn main:api --host 0.0.0.0 --port 30010 --log-level info --reload` - [more options](https://www.uvicorn.org/settings/)

## Access the Server

If you used port `30010` like in the example above then open your browser and enter: `http://localhost:30010/search?q=Nevermind&maxResults=3`. Use IP instead of 'localhost' if your server runs on a different machine.  
The results you will see are given in the official Youtube Data API v3 format or to be more precise a minimal subset of it:
```
{
    "items": [{
        "id": {
            "videoId": "iZ_SwfLlpHo"
        },
        "snippet": {
            "title": "Nevermind",
            "description": "song"
        }
    }, ...]
}
```
