import factory
from src.documents import Product
from tests.factories.user import UserFactory
from faker import Faker

faker = Faker()

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = faker.name().upper()
    user = UserFactory()
