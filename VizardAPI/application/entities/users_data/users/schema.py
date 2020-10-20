from marshmallow import Schema, fields, post_load
from .model import User


class UserSchema(Schema):
    user_id = fields.Integer(data_key="id")

    name = fields.String(data_key="name")

    email = fields.String(data_key="email")

    pass_hash = fields.String(data_key="hash")

    admin_level = fields.Integer(data_key="adm")     # todo create adm lvl

    avatar = fields.String(data_key="avt")

    @post_load
    def load(self, data, **kwargs):
        return User(**data)
