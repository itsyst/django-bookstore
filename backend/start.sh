#!/bin/bash
# Activate the virtual environment
# source .venv/bin/activate -> Local
source /app/.venv/bin/activate

# Run Celery in the background
# celery -A app worker --loglevel=info &

# Run Celery in the background
# celery -A app beat --loglevel=info &

# Run Celery in the background
# celery -A app flower

# Install the dependencies (in case anything was missed during Docker image build)
pip install --no-cache-dir -r /app/requirements.txt

# Run Django migrations
python /app/manage.py migrate

# Run the Django development server
python /app/manage.py runserver 0.0.0.0:8000
