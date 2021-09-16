"""Testing settings.

With these settings, tests run faster.
"""

from .base import *  # NOQA
from .base import env
    
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ROOT_DIR / 'db.sqlite3',
    }
}
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'