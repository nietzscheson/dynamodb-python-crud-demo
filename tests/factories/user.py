import factory
from src.documents import User
from faker import Faker

faker = Faker()

class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = faker.name().upper()
    email = faker.email()
