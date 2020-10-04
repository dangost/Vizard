from marshmallow import fields, Schema, post_load
from application.entities.genres.model import Genre


class GenresSchema(Schema):
    genre_id = fields.Integer(data_key="id", required=False)

    name = fields.String(data_key="name")

    description = fields.String(data_key="desc")

    @post_load
    def load_genre(self, data, **kwargs):
        return Genre(**data)
