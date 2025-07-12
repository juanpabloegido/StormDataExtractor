import requests

KEYWORDS = ["hail", "wind damage", "tree down"]
BACKEND_URL = "http://localhost:8000/events"

# get alerts from api, filter by kw

def scrape_weather_alerts_api():
    url = "https://api.weather.gov/alerts"
    resp = requests.get(url)
    data = resp.json()
    events = []
    for feature in data.get("features", []):
        props = feature.get("properties", {})
        desc = props.get("description") or ""
        title = props.get("headline") or props.get("event") or ""
        location = props.get("areaDesc", "USA")
        issued = props.get("sent")
        alert_id = feature.get("id") or props.get("id")
        found_keywords = [kw for kw in KEYWORDS if kw.lower() in title.lower() or kw.lower() in desc.lower()]
        if found_keywords and alert_id:
            event = {
                "alert_id": alert_id,
                "title": title,
                "location": location,
                "timestamp": issued,
                "keywords": found_keywords,
                "source": "api.weather.gov"
            }
            events.append(event)
    return events

# send events to backend

def send_events(events):
    for event in events:
        r = requests.post(BACKEND_URL, json=event)
        print(f"Sent: {event['title']} | Status: {r.status_code}")

if __name__ == "__main__":
    events = scrape_weather_alerts_api()
    send_events(events) 