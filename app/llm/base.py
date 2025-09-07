from abc import ABC, abstractmethod
from typing import Any, Dict

class LLMProvider(ABC):
    @abstractmethod
    async def generate(self, prompt: str, model: str) -> Dict[str, Any]:
        """Send prompt to model and return response"""
        pass