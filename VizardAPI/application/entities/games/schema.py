from marshmallow import fields, Schema, post_load
from application.entities.games.model import Game


class GamesSchema(Schema):
    game_id = fields.Integer(data_key="id")

    name = fields.String(data_key="name")

    avatar = fields.String(data_key="avt")  # picture link

    trailer = fields.String(data_key="tr")  # yt link

    steam = fields.String(data_key="stm")  # steam link

    torrent = fields.String(data_key="trr")  # torrent link

    rate = fields.Float(data_key="rt")

    price = fields.Float(data_key="prc")

    studio_id = fields.Integer(data_key="stdId")

    genre_id = fields.Integer(data_key="gnrId")

    @post_load
    def load_game(self, data, **kwargs):
        return Game(**data)
