from fastapi import FastAPI
from schemas import ConversationRequest, AnalysisResponse, AnalyzedMessage
from services.sentiment import SentimentAnalyzer
from services.intent import IntentClassifier
import time
import aiohttp
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("my_app")
app = FastAPI()

sentiment_analyzer = SentimentAnalyzer()
intent_classifier = IntentClassifier()

async def async_log(data):
    async with aiohttp.ClientSession() as session:
        await session.post("http://localhost:8001/log", json=data)

@app.post("/predict", response_model=AnalysisResponse)
async def analyze_conversation(payload: ConversationRequest):
    sentence = payload.conversation

    start_sentiment = time.perf_counter()
    try:
        sentiment = sentiment_analyzer.predict(sentence)
    except Exception as E:
        sentiment = ""
        logger.error(f"SentimentAnalyzer Error: {E}")
    sentiment_time = time.perf_counter() - start_sentiment

    start_intent = time.perf_counter()
    try:
        intent = intent_classifier.predict(sentence)
    except Exception as E:
        intent = ""
        logger.error(f"IntentClassifier Error: {E}")
    intent_time = time.perf_counter() - start_intent

    await async_log({
        "sentence": sentence,
        "sentiment": sentiment,
        "intent": intent,
        "sentiment_inference_time": round(intent_time, 4),
        "intent_inference_time": round(sentiment_time, 4)

    })

    result = AnalyzedMessage(
        sentence=sentence,
        sentiment=sentiment,
        intent=intent
    )

    return {"result": result}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
