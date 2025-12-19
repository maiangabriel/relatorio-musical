import psycopg2

def load_supabase(df, database_url):
    conn = psycopg2.connect(database_url)
    cur = conn.cursor()

    query = """
        insert into public.base_musicas
        (run_date, track, artist, album, genre, played_at)
        values (%s, %s, %s, %s, %s, %s)
        on conflict do nothing
    """
    for _, r in df.iterrows():
        cur.execute(
            query,
            (
                r["track"],
                r["artist"],
                r["album"],
                r["genre"],
                r["played_at"],
            )
        )
    conn.commit()
    cur.close()
    conn.close()
