import psycopg2
from datetime import datetime, date

def load_supabase(df, database_url):
    conn = psycopg2.connect(database_url)
    cur = conn.cursor()

    query = """
        INSERT INTO public.base_musicas
        (track, artist, album, genre, played_at)
        VALUES ( %s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING
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
