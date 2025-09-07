from .base import LLMProvider
import openai

class OpenAIProvider(LLMProvider):
    async def generate(self, prompt: str, model: str):
        response = await openai.ChatCompletion.acreate(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.to_dict()