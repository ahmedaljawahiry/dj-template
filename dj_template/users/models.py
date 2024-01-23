"""DB models for the users app"""
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Extends Django's user model"""

    name = CharField(help_text=_("Full name of User"), blank=True, max_length=255)

    def __str__(self):
        return self.username
