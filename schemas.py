from pydantic import BaseModel
from typing import List, Dict

class ConversationRequest(BaseModel):
    conversation: str

class AnalyzedMessage(BaseModel):
    sentence: str
    sentiment: str
    intent: str

class AnalysisResponse(BaseModel):
    result: AnalyzedMessage
