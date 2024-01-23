"""Test factories for the users app"""
from factory import SubFactory
from factory import django as factory_django
from factory import fuzzy

from dj_template.users.models import User


class UserFactory(factory_django.DjangoModelFactory):
    """Factory for the User model"""

    username = fuzzy.FuzzyText()
    email = fuzzy.FuzzyText()

    class Meta:
        model = User
