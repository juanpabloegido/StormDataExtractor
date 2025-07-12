from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# event for storm
class StormEvent(BaseModel):
    alert_id: str
    title: str
    location: str
    timestamp: datetime
    keywords: List[str]
    source: Optional[str] = None
    zipcode: Optional[str] = None
