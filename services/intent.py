from groq import Groq
from config import settings
import json

class IntentClassifier:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = settings.GROQ_MODEL_NAME
        self.system_prompt = """
You are an advanced, expert and clever iPhone conversation analyzer. Your task is to:

1. Analyze each user message about iPhones and classify its intent into one of these categories:
   - greeting
   - inquiry
   - purchase_intent
   - complaint
   - plan_change
   - renewal
   - other

2. Respond in strict JSON format:
{
   "original_message": "user input",
   "analysis": {
      "intent": "classified_intent",
      "confidence": "0-100%"
   }
}

Do not write any information. Just write this json format data. If you fail to predict just give empty json data with keys like that "analysis": {
      "intent": "",
      "confidence": ""
   }. 
"""

    def predict(self, message: str) -> str:
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": message}
            ],
            model=self.model,
        )
        print(response.choices[0].message.content)
        return json.loads(response.choices[0].message.content)["analysis"]["intent"]