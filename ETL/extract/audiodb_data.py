import requests

AUDIODB_URL = "https://www.theaudiodb.com/api/v1/json/123/searchtrack.php"

def extract_genre(artist: str, track: str) -> str | None:
    params = {
        "s": artist,
        "t": track
    }

    try:
        r = requests.get(AUDIODB_URL, params=params, timeout=15)
        r.raise_for_status()

        data = r.json()
        if data and data.get("track"):
            return data["track"][0].get("strGenre")

    except Exception as e:
        print(f"⚠️ AudioDB erro ({artist} - {track}): {e}")

    return None
