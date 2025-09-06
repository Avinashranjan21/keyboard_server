from fastapi import APIRouter
from .models import CommandRequest, CommandResponse
from .handlers import COMMANDS

router = APIRouter()

@router.post("/commands", response_model=CommandResponse)
async def process_command(req: CommandRequest) -> CommandResponse:
    parts = req.command.split(" ", 1)
    cmd, query = parts[0], parts[1] if len(parts) > 1 else ""

    if cmd in COMMANDS:
        handler = COMMANDS[cmd]
        return handler(query)
    return CommandResponse(type="error", result="Unknown command")

@router.get("/")
async def root():
    return {"message": "MCP Smart Keyboard Server"}

@router.get("/mcp/health")
async def mcp_health():
    return {"status": "ok", "message": "MCP server running"}