
import pytest
from src.documents import User, Product, UserIndex
from tests.factories import UserFactory, ProductFactory


@pytest.fixture(scope="function")
def delete_tables():
    """
    Delete all tables.
    """
    User.delete_table() if User.exists() else None
    Product.delete_table() if Product.exists() else None


@pytest.fixture(scope="function", autouse=True)
def create_tables(delete_tables):
    """
    Recreate all tables.
    """
    User.create_table()
    Product.create_table()

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

@pytest.fixture()
def product_fixture():
    fixture = ProductFactory.build()
    user = UserFactory.create()

    _ = {"name":fixture.name, "user":user.id}
    return _

@pytest.fixture()
def add_product(product_fixture):
    def _(**kwargs):
        fixtures = {**product_fixture, **kwargs}
        _ = Product(**fixtures)
        _.save()
        return _
    return _
