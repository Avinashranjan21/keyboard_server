from dotenv import load_dotenv
import os

MCP_PROVIDER = os.getenv("MCP_PROVIDER", "openai")  # or gemini
MCP_MODEL = os.getenv("MCP_MODEL", "gpt-4o-mini")   # default model