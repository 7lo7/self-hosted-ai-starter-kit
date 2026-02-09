import requests
import psycopg2

conn = psycopg2.connect(
    host="self-hosted-ai-starter-kit-postgres-1", 
    dbname="n8n",
    user="lo",
    password="Gillis48!"
)
cur = conn.cursor()

OLLAMA_URL = "http://ollama:11434/api/embeddings"
MODEL = "nomic-embed-text"

cur.execute("""
    SELECT
      userid,
      CONCAT_WS(
        ' ',
        'User:', name, surname || '.',
        'Personality traits:',
        'Openness', O || ',',
        'Conscientiousness', C || ',',
        'Extraversion', E || ',',
        'Agreeableness', A || ',',
        'Neuroticism', N || '.'
      ) AS embedding_text
    FROM behaviour
    WHERE embedding IS NULL;
""")

rows = cur.fetchall()

for userid, text in rows:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": text
        },
        timeout=30
    )
    response.raise_for_status()

    vector = response.json()["embedding"]

    cur.execute(
        "UPDATE behaviour SET embedding = %s WHERE userid = %s",
        (vector, userid)
    )

conn.commit()
cur.close()
conn.close()

print("Behaviour table embeddings created.")
