from marshmallow import fields, Schema, post_load, post_dump
from application.entities.games.model import Game
from application import data_to_snake


class GameSchema(Schema):
    game_id = fields.Integer(data_key="Id", required=False)

    name = fields.String(data_key="Name", required=True)

    avatar = fields.String(data_key="Avatar", required=True)  # picture link

    trailer = fields.String(data_key="Trailer", required=True)  # yt link

    description = fields.String(data_key="Description", required=True)

    platform = fields.String(data_key="Platform", required=True)

    steam = fields.String(data_key="Steam", required=False)  # steam link

    torrent = fields.String(data_key="Torrent", required=False)  # torrent link

    rate = fields.Float(data_key="Rate", required=False)

    price = fields.Float(data_key="Price", required=False)

    studio_id = fields.Integer(data_key="StudioId", required=True)

    genre_id = fields.Integer(data_key="GenreId", required=True)

    system_requirements = fields.String(data_key="SystemRequirements", required=False)

    @post_load
    def load_game(self, data, **kwargs):
        return Game(**data_to_snake(data))
