"""
Settings for (faster) tests.
"""
from .base import *  # noqa

# GENERAL
# ------------------------------------------------------------------------------
LOAD_ERROR_PAGE_URLS = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = "bk+&+nq@e(n$fg0ii1chwo2@%)$n48eg48^wxy69s=riufa8k4"
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# STORAGE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.2/ref/files/storage/
STORAGES["default"]["BACKEND"] = "django.core.files.storage.InMemoryStorage"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
