from app.config import MCP_PROVIDER
from .openai_provider import OpenAIProvider
from .gemini_provider import GeminiProvider

def get_llm_provider():
    if MCP_PROVIDER == "openai":
        return OpenAIProvider()
    elif MCP_PROVIDER == "gemini":
        return GeminiProvider()
    else:
        raise ValueError(f"Unsupported provider: {MCP_PROVIDER}")