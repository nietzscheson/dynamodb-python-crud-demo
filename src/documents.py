import uuid
from datetime import datetime
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model
from src.config import Config

class Resource(Model):
    __abstract__ = True

    id = UnicodeAttribute(hash_key=True, default=lambda: uuid.uuid4().hex)
    created_at = UTCDateTimeAttribute(default=datetime.utcnow)

    @classmethod
    def update(cls, **kwargs):
        for key, value in kwargs.items():
            setattr(cls, key, value)

    def to_json(self):
        return {x: getattr(self, x) for x in self.__dict__["attribute_values"]}


class User(Resource):
    """
    A Table User
    """
    class Meta:
        table_name = "core-user"
        host = Config.DYNAMODB_HOST
        write_capacity_units = 10
        read_capacity_units = 10

    username = UnicodeAttribute()
    email = UnicodeAttribute()

class UserIndex(GlobalSecondaryIndex):
    """
    A Table User Index
    This works like a proxy
    """
    class Meta:
        table_name = "core_user_index"
        host = Config.DYNAMODB_HOST
        write_capacity_units = 1
        read_capacity_units = 1
        projection = AllProjection()

    user = UnicodeAttribute(hash_key=True)

class Product(Resource):
    """
    A Table Product
    """
    class Meta:
        table_name = "core-product"
        host = Config.DYNAMODB_HOST
        write_capacity_units = 1
        read_capacity_units = 1

    name = UnicodeAttribute()
    user_index = UserIndex()
    user = UnicodeAttribute()

