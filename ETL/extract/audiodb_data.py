import requests
from urllib.parse import quote

def extract_genre(api_key, artist, track):
    url = f"https://www.theaudiodb.com/api/v1/json/{api_key}/searchtrack.php"

    params = {
        "s": quote(artist),
        "t": quote(track)
    }

    r = requests.get(url, params=params, timeout=20)
    if r.ok and r.json().get("track"):
        return r.json()["track"][0].get("strGenre")

    return None
