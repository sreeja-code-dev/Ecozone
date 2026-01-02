from fastapi import APIRouter, UploadFile, File, HTTPException
from .models import PredictionResponse, WasteLog
from .services.tips import tip_for
from .services.ai import classify_image_stub
from .db import logs

router = APIRouter()

@router.post("/classify", response_model=PredictionResponse)
async def classify_waste(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload an image file.")

    image_bytes = await file.read()
    label, confidence = classify_image_stub(image_bytes)
    tip = tip_for(label)

    doc = WasteLog(label=label, confidence=confidence, tip=tip, filename=file.filename)
    result = await logs.insert_one(doc.dict())
    return PredictionResponse(label=label, confidence=confidence, tip=tip, saved_id=str(result.inserted_id))