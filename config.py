import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")
    GROQ_MODEL_NAME = "llama3-8b-8192"
    SENTIMENT_MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"

settings = Settings()
