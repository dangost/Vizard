from marshmallow import Schema, fields, post_load
from .model import UserToRates


class UserToRatesSchema(Schema):
    key = fields.Integer(data_key="id")

    user_id = fields.Integer(data_key="uid")

    game_id = fields.Integer(data_key="gid")

    rate = fields.Integer(data_key="rate")

    @post_load
    def load(self, data, **kwargs):
        return UserToRates(**data)
