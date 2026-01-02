from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PredictionResponse(BaseModel):
    label: str
    confidence: float
    tip: str
    saved_id: Optional[str] = None

class WasteLog(BaseModel):
    label: str
    confidence: float
    tip: str
    filename: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    user_id: Optional[str] = None