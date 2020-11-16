from marshmallow import fields, Schema, post_load, post_dump
from application.entities.games.model import Game


class GameSchema(Schema):
    game_id = fields.Integer(data_key="id", required=False)

    name = fields.String(data_key="name", required=True)

    avatar = fields.String(data_key="avt", required=True)  # picture link

    trailer = fields.String(data_key="tr", required=True)  # yt link

    description = fields.String(data_key="desc", required=True)

    platform = fields.String(data_key="os", required=True)

    steam = fields.String(data_key="stm", required=False)  # steam link

    torrent = fields.String(data_key="trr", required=False)  # torrent link

    rate = fields.Float(data_key="rt", required=False)

    price = fields.Float(data_key="prc", required=False)

    studio_id = fields.Integer(data_key="stdId", required=True)

    genre_id = fields.Integer(data_key="gnrId", required=True)

    system_requirements = fields.String(data_key="sys", required=False)

    @post_load
    def load_game(self, data, **kwargs):
        return Game(**data)
