from marshmallows import Schema, fields
from pprint import pprint
import datetime as dt
from collections import OrderedDict

from marshmallows import ValidationError


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)
class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()


try:
    result = UserSchema().load({"name": "John", "email": "foo"})
except ValidationError as err:
    print(err.messages)  # => {"email": ['"foo" is not a valid email address.']}
    print(err.valid_data)  # => {"name": "John"}