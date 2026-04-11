FROM python:3.10-slim        # ✅ smaller image (~50% lighter)

WORKDIR /app

# ✅ Copy requirements first for Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ✅ Don't run as root
RUN useradd -m appuser
USER appuser

HEALTHCHECK CMD curl --fail http://localhost:7860/state || exit 1

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
