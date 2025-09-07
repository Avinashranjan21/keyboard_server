from .base import LLMProvider
import google.generativeai as genai

class GeminiProvider(LLMProvider):
    async def generate(self, prompt: str, model: str):
        model_obj = genai.GenerativeModel(model)
        response = await model_obj.generate_content_async(prompt)
        return {"text": response.text}