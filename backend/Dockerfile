# use python image
FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y cron procps \
    && pip install --no-cache-dir fastapi uvicorn pymongo requests \
    && rm -rf /var/lib/apt/lists/*

# Add crontab file
COPY crontab /etc/cron.d/stormscraper
RUN chmod 0644 /etc/cron.d/stormscraper && crontab /etc/cron.d/stormscraper

# Create log file
RUN touch /var/log/cron.log

CMD ["sh", "-c", "cron && uvicorn main:app --host 0.0.0.0 --port 8000"] 