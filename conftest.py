"""Global pytest config and fixtures"""
import pytest

pytest_plugins = [
    "dj_template.users.tests.fixtures",
]


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """All tests can access the DB"""
    pass
