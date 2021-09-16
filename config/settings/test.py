"""Testing settings.

With these settings, tests run faster.
"""

from .base import *  # NOQA
from .base import env

SECRET_KEY = env('DJANGO_SECRET_KEY', default='django-insecure-xc(z*pb-vf#+3m+24et$2dxtf!_^l635k*=%t2^24$dmkl_3c7')
# TEST_RUNNER = "django.test.runner.DiscoverRunner"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': f"{ROOT_DIR}/db.sqlite3",
    }
}
