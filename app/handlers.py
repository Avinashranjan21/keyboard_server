from .models import CommandResponse
from typing import Callable
from app.llm.factory import get_llm_provider
from app.config import MCP_MODEL

# ---- MCP Integration Placeholder ----
# In real usage, this will connect to your MCP runtime
# and call tools like weather, translation, etc.
# For now, we simulate it.
def call_mcp_tool(tool: str, query: str) -> str:
    # TODO: Replace this with actual MCP SDK call
    # Example: await mcp_client.run_tool("weather", {"location": query})
    return f"[MCP] Executed {tool} with query: {query}"

async def handle_ai_command(prompt: str):
    provider = get_llm_provider()
    return await provider.generate(prompt, MCP_MODEL)

# ---- Command Handlers ----
def handle_weather(query: str) -> CommandResponse:
    result = call_mcp_tool("weather", query)
    return CommandResponse(type="weather", result=result)

def handle_time_conversion(query: str) -> CommandResponse:
    result = call_mcp_tool("time_conversion", query)
    return CommandResponse(type="time_conversion", result=result)

def handle_currency_conversion(query: str) -> CommandResponse:
    result = call_mcp_tool("currency_conversion", query)
    return CommandResponse(type="currency_conversion", result=result)

def handle_translation(query: str) -> CommandResponse:
    result = call_mcp_tool("translation", query)
    return CommandResponse(type="translation", result=result)

async def handle_ai_command(query: str) -> CommandResponse:
    provider = get_llm_provider()
    ai_response = await provider.generate(query, MCP_MODEL)
    return CommandResponse(type="ai", result=ai_response)



# ---- Command Registry ----
COMMANDS: dict[str, Callable[[str], CommandResponse]] = {
    "/weather": handle_weather,
    "/time": handle_time_conversion,
    "/currency": handle_currency_conversion,
    "/translate": handle_translation,
    "/ai": handle_ai_command,
}