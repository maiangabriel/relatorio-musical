import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

TIMEZONE = ZoneInfo("America/Sao_Paulo")

def transform_tracks(raw_tracks, genre_func):
    rows = []
   

    for t in raw_tracks:
        # Ignora música "now playing" (não tem timestamp)
        if "@attr" in t and t["@attr"].get("nowplaying") == "true":
            continue
        
        played_at = datetime.fromtimestamp(
            int(t["date"]["uts"]),
            tz=TIMEZONE)

        rows.append({
            "track": t["name"],
            "artist": t["artist"]["#text"],
            "album": t["album"]["#text"],
            "played_at": played_at,
            "genre": genre_func(
                t["artist"]["#text"],
                t["name"]
            )
        })

    return pd.DataFrame(rows)