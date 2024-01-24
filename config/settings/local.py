"""
Settings for local development.
"""
import socket

from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True
LOAD_ERROR_PAGE_URLS = True
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST_USER = "debug"
EMAIL_HOST_PASSWORD = "debug"

# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
# https://github.com/jazzband/django-debug-toolbar/issues/1854
INTERNAL_IPS = type("c", (), {"__contains__": lambda *a: True})()

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa F405

# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-eager-propagates
CELERY_TASK_EAGER_PROPAGATES = True
