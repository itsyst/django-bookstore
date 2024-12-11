# Backend Dockerfile
FROM python:3.11-slim

# Install system dependencies required for psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Create the virtual environment
RUN python -m venv .venv

# Copy the backend app files into the container
COPY . /app/

# Expose the necessary port
EXPOSE 8000

# Set the entry point to the script that starts both Celery and Django
CMD ["/app/start.sh"]
