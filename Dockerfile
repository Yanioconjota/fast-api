# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Load default values for environment variables (optional)
ENV APP_HOST=0.0.0.0
ENV APP_PORT=8000

# Use sh -c to expand variables
CMD ["sh", "-c", "uvicorn app.main:app --host $APP_HOST --port $APP_PORT --reload"]
