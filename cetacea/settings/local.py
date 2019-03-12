from .base import *
from .base import env

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, env('SQLITE_NAME')),
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

from .components.aws_storage import *

# STATIC_URL = '/static/'

# MEDIA_URL = 'http://cetacea-backend-static.s3-website.us-east-2.amazonaws.com/media/'