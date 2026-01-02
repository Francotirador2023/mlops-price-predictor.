FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY model.joblib .

# Expose API port
EXPOSE 8000

# Command to run API
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
