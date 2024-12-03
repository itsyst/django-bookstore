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

# Run the Django development server
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
