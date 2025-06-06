# app/main.py
import os
import json
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from utils.forward import forward_to_storage
import httpx
import traceback

# Load environment variables from the .env file
load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "Default App"))
ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
ollama_url = f"{ollama_host}/api/generate"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://frontend:5173"],  # o ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "app_name": os.getenv("APP_NAME"),
        "env": os.getenv("APP_ENV"),
        "host": os.getenv("APP_HOST"),
        "port": os.getenv("APP_PORT"),
        "message": "Vamooo Ñubeeeeeeee"
    }

# Ask Ollama API for a response
@app.get("/joker", summary="Get a joke from the Joker API")
def ask_ollama():
    payload = {
        "model": "llama3",
        "prompt": "Please tell me a joke"
    }

    response = requests.post(ollama_url, json=payload, stream=True)

    output = ""
    for line in response.iter_lines():
        if line:
            try:
                data = line.decode("utf-8")
                chunk = json.loads(data)
                output += chunk.get("response", "")
            except Exception as e:
                print("❌ Error decoding chunk:", e)

    return {"result": output}

# POST version: dynamic prompt
class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask", summary="Ask with custom prompt and forward to storage", description="Send a prompt to Ollama and forward the response to storage.")
async def ask_ollama_dynamic(request: PromptRequest):
    payload = {
        "model": "llama3",
        "prompt": request.prompt,
        "stream": False
    }

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(ollama_url, json=payload, timeout=60.0)
            response.raise_for_status()
            data = response.json()
            result = data.get("response", "")

            # Forward to storage microservice
            await forward_to_storage(prompt=request.prompt, response=result)

            return {"response": result}

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
