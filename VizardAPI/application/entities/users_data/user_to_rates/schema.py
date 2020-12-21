from marshmallow import Schema, fields, post_load

from application import data_to_snake
from .model import UserToRates


class UserToRatesSchema(Schema):
    key = fields.Integer(data_key="Id")

    user_id = fields.Integer(data_key="UserId")

    game_id = fields.Integer(data_key="GameId")

    rate = fields.Integer(data_key="Rate")

    @post_load
    def load(self, data, **kwargs):
        return UserToRates(**data_to_snake(data))
