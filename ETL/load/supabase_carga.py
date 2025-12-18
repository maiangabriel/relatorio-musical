import psycopg2

def load_supabase(df, database_url):
    conn = psycopg2.connect(database_url)
    cur = conn.cursor()

    query = """
        insert into daily_data
        (run_date, track, artist, album, genre, played_at)
        values (%s, %s, %s, %s, %s, %s)
        on conflict do nothing
    """

    for _, r in df.iterrows():
        cur.execute(query, tuple(r))

    conn.commit()
    cur.close()
    conn.close()
