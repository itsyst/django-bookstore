import dj_database_url
import os
from .common import *

DEBUG = False

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
SECRET_KEY = os.environ['SECRET_KEY']


REDIS_URL=os.getenv('REDIS_URL')
CELERY_BROKER_URL = REDIS_URL  # Use the service name 'redis' defined in docker-compose.yml
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,  # (Docker)
        'TIMEOUT': 10 * 60,  
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}