"""Development settings."""

from .base import *  # NOQA
from .base import env

# Base
DEBUG = True

# Security
SECRET_KEY = env('DJANGO_SECRET_KEY', default='django-insecure-xc(z*pb-vf#+3m+24et$2dxtf!_^l635k*=%t2^24$dmkl_3c7')
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# django-extensions
INSTALLED_APPS += [
    
]
