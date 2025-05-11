from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from config import settings
import torch

class SentimentAnalyzer:
    def __init__(self):
        model_name = settings.SENTIMENT_MODEL_NAME
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.labels = ['negative', 'neutral', 'positive']

    def predict(self, text: str) -> str:
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        scores = softmax(outputs.logits.numpy()[0])
        return self.labels[scores.argmax()]
