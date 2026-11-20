FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

# Install dependencies first for layer caching
COPY UI/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit app
COPY UI/streamlit.py .

# Run as a non-root user
RUN useradd --create-home appuser && chown -R appuser /code
USER appuser

EXPOSE 8501

CMD ["streamlit", "run", "streamlit.py", \
     "--server.address=0.0.0.0", \
     "--server.port=8501", \
     "--server.headless=true"]