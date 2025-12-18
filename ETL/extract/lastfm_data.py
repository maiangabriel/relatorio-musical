import requests
from datetime import datetime, timedelta

LASTFM_URL = "https://ws.audioscrobbler.com/2.0/"

def extract_lastfm(api_key, user):
    inicio = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    fim = inicio + timedelta(days=1)

    params = {
        "method": "user.getrecenttracks",
        "user": user,
        "api_key": api_key,
        "format": "json",
        "from": int(inicio.timestamp()),
        "to": int(fim.timestamp()),
        "limit": 200
    }

    r = requests.get(LASTFM_URL, params=params, timeout=30)
    r.raise_for_status()

    return r.json()["recenttracks"]["track"]
