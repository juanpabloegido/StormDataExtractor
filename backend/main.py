from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from models import StormEvent
from db import get_events_collection
from pymongo.errors import PyMongoError, DuplicateKeyError
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# get events, maybe filter by kw
@app.get("/events", response_model=List[StormEvent])
def get_recent_events(keyword: Optional[str] = Query(None)):
    col = get_events_collection()
    query = {}
    if keyword:
        query = {"keywords": keyword}
    docs = col.find(query).sort("timestamp", -1).limit(10)
    return [StormEvent(**doc) for doc in docs]

# add event, skip if duplicate
@app.post("/events", response_model=StormEvent)
def add_event(event: StormEvent):
    col = get_events_collection()
    try:
        col.insert_one(event.dict())
        return event
    except DuplicateKeyError:
        return event
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
