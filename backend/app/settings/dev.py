from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qewn-bz%peq236z^ehm1w)0lb2he!9&udqyf+#!_13ks2(s*ux'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MIDDLEWARE += ['silk.middleware.SilkyMiddleware']
MIDDLEWARE.append('silk.middleware.SilkyMiddleware')

# CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_BROKER_URL = 'redis://redis:6379/0'  # Use the service name 'redis' defined in docker-compose.yml
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 'LOCATION': 'redis://127.0.0.1:6379/0',  # Update with your Redis server's URL
        'LOCATION': 'redis://redis:6379/0',  # (Docker)
        'TIMEOUT': 10,  # Cache out in 10 seconds
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'app.sqlite3',
    }
}

# EMAIL_HOST = 'localhost'
EMAIL_HOST = 'smtp4dev'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False 
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''