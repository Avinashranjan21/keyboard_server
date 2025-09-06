# MCP Server for Smart Keyboard

This is a FastAPI-based MCP server that powers the Flutter Smart Keyboard app.  
The server provides a `/commands` endpoint to handle natural-language commands typed in the keyboard such as:

- `/weather Paris` → Get current weather in Paris  
- `/time 10:30 EST to IST` → Timezone conversion  
- `/currency 100 USD to INR` → Currency conversion  
- `/translate Hello to French` → Language translation  

The MCP server acts as the "brain" of the keyboard — it parses commands, calls APIs or logic, and returns structured responses that the Flutter keyboard client can display or insert into the text field.

---

## Tech Stack
- FastAPI (Python web framework)  
- uv (for Python version + virtual environment management)  
- SQLite (for simple persistence, optional)  

---

## Setup Instructions

### 1. Create and Activate Virtual Environment
First, install `uv` if you don't have it already:
```bash
pip install uv
```
Then, create and activate a virtual environment:
```bash
# Create the virtual environment
uv venv .venv

# Activate the environment
source .venv/bin/activate   # Linux / macOS
# .venv\Scripts\activate      # Windows PowerShell
```

### 2. Install Dependencies
With the virtual environment activated, install the required packages:
```bash
uv pip install fastapi uvicorn requests
```

### 3. Run the Development Server
Finally, start the FastAPI server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```