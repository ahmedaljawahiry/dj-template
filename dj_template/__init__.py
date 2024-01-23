"""
Ensure Celery is available when Django starts.
https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#using-celery-with-django
"""
from config.celery import app as celery_app

__all__ = ("celery_app",)
