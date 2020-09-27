from marshmallow import fields, Schema, post_load
from application.entities.games.model import Game


class GamesSchema(Schema):
    id = fields.Integer(data_key="id")

    name = fields.Integer(data_key="name")

    avatar = fields.String(data_key="avt")  # picture link

    trailer = fields.String(data_key="tr")  # yt link

    steam = fields.String(data_key="stm")  # steam link

    torrent = fields.String(data_key="trr")  # torrent link

    rate = fields.Float(data_key="rt")

    price = fields.Float(data_key="prc")

    @post_load
    def load_game(self, data, **kwargs):
        return Game(**data)
