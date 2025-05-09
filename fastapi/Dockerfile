FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY fastapi/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the FastAPI app
COPY fastapi/app.py .

EXPOSE 8000

# Start FastAPI with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
