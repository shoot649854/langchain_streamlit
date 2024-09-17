# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    python3-dev \
    build-essential \
    && apt-get clean

# Copy the requirements.txt file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --only=main -r requirements.txt
# RUN pip3 install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port
EXPOSE 8080

# Command to run the Streamlit app
CMD ["python3", "-m", "streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
