# create to embedd the data in the table 
import requests
import psycopg2
import json

# PostgreSQL connection
conn = psycopg2.connect(
    host="postgres",      # Container hostname in the Docker network
    dbname="your_db",
    user="postgres",
    password="your_password"
)
cur = conn.cursor()

# Ollama endpoint
OLLAMA_URL = "http://ollama:11434/embed"  # Ollama embedding API

# Fetch rows that need embeddings
cur.execute("SELECT id, text_column FROM my_table WHERE embedding IS NULL;")
rows = cur.fetchall()

for row in rows:
    row_id, text = row
    
    # Call Ollama embedding API
    response = requests.post(
        OLLAMA_URL,
        json={"model": "llama3.2", "text": text}
    )
    
    response.raise_for_status()
    vector = response.json()["embedding"]  # Ollama returns embedding as list
    
    # Update table
    cur.execute(
        "UPDATE my_table SET embedding = %s WHERE id = %s",
        (vector, row_id)
    )

conn.commit()
cur.close()
conn.close()
print("All embeddings added!")
