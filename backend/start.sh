#!/bin/bash
# Activate the virtual environment
source /app/.venv/bin/activate

# Run Celery worker in the background
# celery -A app worker --pool=solo --loglevel=info &

# Run Flower for monitoring
# celery -A app flower --port=5555 &

# Install dependencies
pip install --no-cache-dir -r /app/requirements.txt

# Prepare static directories 
python /app/manage.py collectstatic --noinput

# Run Django migrations
python /app/manage.py migrate

# Run the Django development server
python /app/manage.py runserver 0.0.0.0:8000
