from marshmallow import Schema, fields, post_load

from application import data_to_snake
from .model import User, UserAuth


class UserSchema(Schema):
    user_id = fields.Integer(data_key="Id")

    name = fields.String(data_key="Name", required=True)

    email = fields.String(data_key="Email", required=True)

    pass_hash = fields.String(data_key="PassHash", required=True)

    admin_level = fields.Integer(data_key="AdminLevel")     # todo create adm lvl

    avatar = fields.String(data_key="Avatar")

    telegram = fields.String(data_key="Telegram")

    steam = fields.String(data_key="Steam")

    @post_load
    def load(self, data, **kwargs):
        return User(**data_to_snake(data))


class UserAuntSchema(Schema):
    email = fields.String(data_key="Email")

    pass_hash = fields.String(data_key="PassHash")

    @post_load
    def load(self, data, **kwargs):
        return UserAuth(**data_to_snake(data))
