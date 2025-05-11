# log_server.py
from fastapi import FastAPI
from pydantic import BaseModel
from log_db import log_analysis

log_app = FastAPI()

class LogItem(BaseModel):
    component: str
    sentence: str
    sentiment: str | None = None
    intent: str | None = None
    sentiment_inference_time: float
    intent_inference_time: float

@log_app.post("/log")
async def log_endpoint(item: LogItem):
    await log_analysis(item.dict())
    return {"status": "logged"}
