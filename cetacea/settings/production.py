from .base import *
from .base import env

# SECURITY WARNING: this should be changed to False... soon!
DEBUG = True

ALLOWED_HOSTS = ['*']


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': env('MYSQL_NAME'),
#         'USER': env('MYSQL_USER'),
#         'PASSWORD': env('MYSQL_PASSWORD'),
#         'HOST': env('MYSQL_HOST'),
#         'PORT': env('MYSQL_PORT'),
#     }
# }

from .components.aws_storage import *