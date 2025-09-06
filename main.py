from fastapi import FastAPI
from app.api import router

def create_app() -> FastAPI:
    app = FastAPI(
        title="MCP Smart Keyboard Server",
        description="FastAPI backend to handle keyboard commands via MCP",
        version="1.0.0"
    )

    # Register routes
    app.include_router(router)
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)