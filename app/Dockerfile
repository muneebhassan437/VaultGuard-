
FROM python:3.13-slim

# Don't write .pyc files; send logs straight to the console
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MODEL_PATH=/code/models/logistic_regression_model.joblib

# Run from inside app/ so "from validation import ..." keeps working
WORKDIR /code/app

# Install dependencies first so this layer stays cached when only code changes
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API code and the trained model
COPY app/ /code/app/
COPY models/logistic_regression_model.joblib /code/models/

# Run as a non-root user
RUN useradd --create-home appuser && chown -R appuser /code
USER appuser

EXPOSE 8000

# 0.0.0.0 makes the API reachable from outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]