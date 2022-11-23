import uuid
from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model
from src.config import Config

class Resource(Model):
    __abstract__ = True

    id = UnicodeAttribute(hash_key=True, default=lambda: uuid.uuid4().hex)
    created_at = UTCDateTimeAttribute(default=datetime.utcnow)

    @classmethod
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

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
