"""Test fixtures for the users app"""
import uuid

import pytest
from django.test import Client

from dj_template.users.models import User


@pytest.fixture()
def user_unauthenticated() -> User:
    """An unauthenticated user"""
    return User.objects.create_user(username="un-auth-user", password="p1234")


@pytest.fixture()
def user_standard(client) -> User:
    """An authenticated (via session) user"""
    user = User.objects.create_user(username="standard-user", password="p1351")
    client.force_login(user)
    return user


@pytest.fixture()
def user_staff(client, admin_user) -> User:
    """An authenticated (via session) staff user"""
    user = User.objects.create_user(
        username="admin-user", password="p51015", is_staff=True
    )
    client.force_login(user)
    return user


@pytest.fixture()
def user_super(client) -> User:
    """An authenticated (via session) superuser"""
    user = User.objects.create_user(
        username="superuser", password="p4414", is_superuser=True
    )
    client.force_login(user)
    return user


@pytest.fixture()
def client_standard(user_standard):
    """A client for a standard, authenticated, user"""
    # avoid the client fixture since other fixtures use it to log users in
    client = Client()
    client.force_login(user_standard)
    return client


@pytest.fixture()
def client_admin(user_admin):
    """A client for an authenticated admin user"""
    # avoid the client fixture since other fixtures use it to log users in
    client = Client()
    client.force_login(user_admin)
    return client


@pytest.fixture()
def client_super(user_super):
    """A client for an authenticated superuser"""
    # avoid the client fixture since other fixtures use it to log users in
    client = Client()
    client.force_login(user_super)
    return client


@pytest.fixture()
def client_unauthenticated():
    """Returns a client that is logged out"""
    # avoid the client fixture since other fixtures use it to log users in
    client = Client()
    client.logout()
    return client
