import pandas as pd
from datetime import datetime

def transform_tracks(raw_tracks, genre_func):
    rows = []

    for t in raw_tracks:
        # Ignora músicas "now playing"
        if "date" not in t:
            continue

        rows.append({
            "track": t["name"],
            "artist": t["artist"]["#text"],
            "album": t["album"]["#text"],
            "played_at": datetime.fromtimestamp(
                int(t["date"]["uts"])
            ),
            "genre": genre_func(
                t["artist"]["#text"],
                t["name"]
            )
        })

    return rows