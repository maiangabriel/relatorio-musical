from psycopg2.extras import execute_batch

def load_supabase(df, cur):
    query = """
        INSERT INTO tracks_played
        (track, artist, album, genre, played_at)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
    """

    data = [
        (
            r["track"],
            r["artist"],
            r["album"],
            r["genre"],
            r["played_at"],
        )
        for _, r in df.iterrows()
    ]

    execute_batch(cur, query, data, page_size=100)
