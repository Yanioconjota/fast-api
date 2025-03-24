# app/main.py
import os
import json
import requests
from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "Default App"))

@app.get("/")
def read_root():
    return {
        "app_name": os.getenv("APP_NAME"),
        "env": os.getenv("APP_ENV"),
        "host": os.getenv("APP_HOST"),
        "port": os.getenv("APP_PORT"),
        "message": "Vamooo Ñubeeeeeeee"
    }

@app.get("/ask")
def ask_ollama():
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": "Why is the sky blue?"
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