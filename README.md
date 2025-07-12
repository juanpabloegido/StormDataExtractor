# Storm Data Extractor

This app get storm alerts from US and show in a nice dashboard. You can filter by keyword. Data is save in MongoDB Atlas.

## How run

You need Docker and Docker Compose.

1. Clone this repo
2. Build and run all:

```
docker-compose up --build
```

- Backend: [http://localhost:8000/docs](http://localhost:8000/docs)
- Frontend: [http://localhost:3000](http://localhost:3000)

## How it work
- Scraper get alerts from https://api.weather.gov/alerts
- Only save alerts with keywords: hail, wind damage, tree down
- No duplicate alerts (use alert_id)
- Frontend show last 10 alerts, you can filter by keyword
- Scraper run auto every 10 min (cronjob inside backend container)

## Config
- MongoDB Atlas url is in docker-compose.yml, you can change for your own

## Author
Juan Egido 