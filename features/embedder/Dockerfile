# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy Python script into container
COPY embedder.py /app/embedder.py

# Install dependencies
RUN pip install --no-cache-dir psycopg2-binary requests

# Run the script by default
CMD ["python", "/app/embedder.py"]
