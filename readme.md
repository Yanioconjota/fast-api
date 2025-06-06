# 🚀 FastAPI Starter Project

This is a basic FastAPI application configured to run both locally and inside a Docker container, using environment variables for flexibility and clean structure.

---

## 📦 Features

- ⚡ FastAPI with automatic Swagger UI
- 🐳 Docker and Docker Compose ready
- 🔧 Environment variables via `.env`
- 🔁 Hot-reload enabled for development

---

## 🏗️ Project Structure

```text
fast-api/
├── app/
│   └── main.py               # Main FastAPI application
├── venv/                     # Local virtual environment (optional)
├── .env                      # Environment variables (not committed)
├── .env.template             # Sample environment file
├── .gitignore                # Git ignore rules
├── .dockerignore             # Docker ignore rules
├── Dockerfile                # Docker build config
├── docker-compose.yml        # Docker Compose config
└── requirements.txt          # Python dependencies
```

## 🪛 Install Ollama
> This project uses [Ollama](https://ollama.com/) locally to run LLMs such as llama3:7b. You do not need a GPU to run the model, but performance may vary on CPU.

1. Download and install Ollama from the official website 👉 https://ollama.com/download
2. Once installed, open a terminal and verify:
  ```
  ollama --version
  ```
3. Run the Ollama server (usually starts automatically):
  ```
  ollama serve
  ```
4. Pull the `llama3` model:
  ```
  ollama pull llama3
  ```
5. Now you can query Ollama from FastAPI at:
  ```
  http://localhost:11434/api/generate
  
  ```
  ℹ️ You can test it manually using curl:
  ```bash
  curl http://localhost:11434/api/generate -d '{
    "model": "llama3",
    "prompt": "Why is the sky blue?"
  }'
  
  ```

## 🚀 Getting Started

### ▶️ Run Locally

1. Create and activate virtual environment:

  ```bash
  py -m venv venv
  source venv/Scripts/activate  # or venv\Scripts\activate on Windows
  ```

2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
3. Run the app:
  ```bash
  uvicorn app.main:app --reload
  ```
  > Optinally: 🐳 Buid and start a Docker container instead

  ```bash
  docker-compose up --build
  ```
4. The app will be avalable in:
  - http://localhost:8000
  - http://localhost:8000/docs
  - http://localhost:8000/redoc

---

⚙️ Environment Variables
```bash
APP_NAME=FastAPI App
APP_ENV=development
APP_HOST=0.0.0.0
APP_PORT=8000
```
