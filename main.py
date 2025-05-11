from fastapi import FastAPI
from schemas import ConversationRequest, AnalysisResponse, AnalyzedMessage
from services.sentiment import SentimentAnalyzer
from services.intent import IntentClassifier
import time
import aiohttp

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
    sentiment = sentiment_analyzer.predict(sentence)
    sentiment_time = time.perf_counter() - start_sentiment

    start_intent = time.perf_counter()
    intent = intent_classifier.predict(sentence)
    intent_time = time.perf_counter() - start_intent

    await async_log({
        "component": "intent",
        "sentence": sentence,
        "sentiment" sentiment,
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
