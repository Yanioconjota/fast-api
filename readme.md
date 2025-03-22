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

fast-api/ │ ├── app/ │ └── main.py # Main FastAPI application │ ├── venv/ # Local virtual environment (optional) ├── .env # Environment variables (not committed) ├── .env.template # Sample environment file ├── .gitignore # Git ignore rules ├── .dockerignore # Docker ignore rules ├── Dockerfile # Docker build config ├── docker-compose.yml # Docker Compose config └── requirements.txt # Python dependencies

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
