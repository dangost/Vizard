from marshmallow import fields, Schema, post_load
from application.entities.genres.model import Genre
from application import data_to_snake


class GenresSchema(Schema):
    genre_id = fields.Integer(data_key="Id", required=False)

    name = fields.String(data_key="Name", required=True)

    description = fields.String(data_key="Description", required=True)

    @post_load
    def load_genre(self, data, **kwargs):
        return Genre(**data_to_snake(data))
