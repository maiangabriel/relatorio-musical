import os
from etl.extract.lastfm_data import extract_lastfm
from etl.extract.audiodb_data import extract_genre
from etl.transform.tracks_data import transform_tracks
from etl.load.supabase_carga import load_supabase

def main():
    raw = extract_lastfm(
        api_key=os.getenv("LASTFM_API_KEY"),
        user=os.getenv("LASTFM_USERNAME")
    )

    df = transform_tracks(
        raw,
        genre_func=lambda a, t: extract_genre(
            os.getenv("AUDIO_DB_API_KEY"), a, t
        )
    )

    load_supabase(df, os.getenv("DATABASE_URL"))

    print("✅ ETL diário executado com sucesso")

if __name__ == "__main__":
    main()