# app/main.py
import os
import json
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


# Load environment variables from the .env file
load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "Default App"))
ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # o ["*"] for testing
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
    url = ollama_host + "/api/generate"
    payload = {
        "model": "llama3",
        "prompt": "Please tell me a joke"
    }

    # Send the request to the Ollama API
    response = requests.post(url, json=payload, stream=True)

    # Process the response and return the result
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

@app.post("/ask", summary="Ask with custom prompt", description="Send a prompt to the local Ollama server using llama3.")
def ask_ollama_dynamic(request: PromptRequest):
    url = ollama_host + "/api/generate"
    payload = {
        "model": "llama3",
        "prompt": request.prompt
    }

    response = requests.post(url, json=payload, stream=True)

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