# ---- Base Image ----
FROM python:3.11-slim AS base

# Set working directory
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt /app/

# ---- Dependencies ----
FROM base AS dependencies

# Install system dependencies and Python dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --only=main -r requirements.txt

# ---- Final Image ----
FROM base AS release

# Copy installed dependencies from dependencies stage
COPY --from=dependencies /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=dependencies /usr/local/bin /usr/local/bin

# Copy the rest of the application code
COPY . .

# Expose the port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["python3", "-m", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
