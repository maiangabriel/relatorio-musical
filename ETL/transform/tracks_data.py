import pandas as pd
from datetime import datetime

def transform_tracks(raw_tracks, genre_func):
    rows = []

    for t in raw_tracks:
        rows.append({
            "track": t["name"],
            "artist": t["artist"]["#text"],
            "album": t["album"]["#text"],
            "played_at": datetime.fromtimestamp(int(t["date"]["uts"])),
            "genre": genre_func(t["artist"]["#text"], t["name"])
        })

    df = pd.DataFrame(rows)

    df = df.drop_duplicates(subset=["track", "artist", "played_at"])
    df["run_date"] = datetime.now().date()

    return df
