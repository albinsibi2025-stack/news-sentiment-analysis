import os
import psycopg2

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        database=os.getenv("DB_NAME", "newsdb"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "root")
    )

def insert_news(title, description, source, published_at, label, score):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO news
        (title, description, source, published_at, sentiment_label, sentiment_score)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (title, description, source, published_at, label, score))

    conn.commit()
    cur.close()
    conn.close()