from marshmallow import fields, Schema, post_load, post_dump
from application.entities.games.model import Game


class GamesSchema(Schema):
    game_id = fields.Integer(data_key="id", required=False)

    name = fields.String(data_key="name")

    avatar = fields.String(data_key="avt")  # picture link

    trailer = fields.String(data_key="tr")  # yt link

    description = fields.String(data_key="desc")

    platform = fields.String(data_key="os")

    steam = fields.String(data_key="stm", required=False)  # steam link

    torrent = fields.String(data_key="trr", required=False)  # torrent link

    rate = fields.Float(data_key="rt")

    price = fields.Float(data_key="prc")

    studio_id = fields.Integer(data_key="stdId")

    genre_id = fields.Integer(data_key="gnrId")

    system_requirements = fields.String(data_key="sys", required=False)

    @post_load
    def load_game(self, data, **kwargs):
        return Game(**data)
