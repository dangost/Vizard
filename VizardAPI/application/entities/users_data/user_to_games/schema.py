from marshmallow import Schema, fields, post_load
from .model import UserToGames


class UserToGamesSchema(Schema):
    key = fields.Integer(data_key="key")
    user_id = fields.Integer(data_key="uid")
    game_id = fields.Integer(data_key="gid")

    @post_load
    def load(self, data, **kwargs):
        return UserToGames(**data)
