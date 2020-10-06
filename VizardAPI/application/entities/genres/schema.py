from marshmallow import fields, Schema, post_load
from application.entities.genres.model import Genre


class GenresSchema(Schema):
    genre_id = fields.Integer(data_key="id", required=False)

    name = fields.String(data_key="name", required=True)

    description = fields.String(data_key="desc", required=True)

    @post_load
    def load_genre(self, data, **kwargs):
        return Genre(**data)
