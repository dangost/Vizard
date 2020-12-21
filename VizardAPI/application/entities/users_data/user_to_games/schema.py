from marshmallow import Schema, fields, post_load
from .model import UserToGames
from application import data_to_snake


class UserToGamesSchema(Schema):
    key = fields.Integer(data_key="Id")
    user_id = fields.Integer(data_key="UserId")
    game_id = fields.Integer(data_key="GameId")

    @post_load
    def load(self, data, **kwargs):
        return UserToGames(**data_to_snake(data))
