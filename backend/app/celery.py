import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','app.settings.dev')

celery = Celery('app')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()


# docker run -d -p 6379:6379 redis
# docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
# celery -A app worker --loglevel=info


# # Running Your Project Using Windows
# # Subsystem for Linux (WSL)
# Install WSL wsl --install -d ubuntu
# Install VSCode Extension Remote-WSL: Reopen Folder in WSL.
# Update the Package List sudo apt update && sudo apt upgrade
# sudo add-apt-repository ppa:deadsnakes/ppa
# sudo apt install python
# Install pip and pipenv 
# Install & Configure MySQL/PostgreSQL ... etc
# Start the Project  
# install the project dependencies:
# pipenv install
# Activate the virtual environment:
# pipenv shell
# Run the migrations:
# python manage.py migrate
# Optionally, seed the database:
# python manage.py seed_db
# Start the web server:
# python manage.py runserver

