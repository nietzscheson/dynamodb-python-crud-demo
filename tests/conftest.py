
import pytest
from src.documents import User
from tests.factories import UserFactory


@pytest.fixture(scope="function")
def delete_tables():
    """
    Delete all tables.
    """
    User.delete_table() if User.exists() else None


@pytest.fixture(scope="function", autouse=True)
def create_tables(delete_tables):
    """
    Recreate all tables.
    """
    User.create_table()

@pytest.fixture()
def user_fixture():
    fixture = UserFactory.build()
    _ = {"username":fixture.username, "email":fixture.email}
    return _

@pytest.fixture()
def add_user(user_fixture):
    def _(**kwargs):
        fixtures = {**user_fixture, **kwargs}
        _ = User(**fixtures)
        _.save()
        return _
    return _
