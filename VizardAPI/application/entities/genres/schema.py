from marshmallow import fields, Schema, post_load
from application.entities.genres.model import Genre


class GenresSchema(Schema):
    id = fields.Integer(data_key="id")

    name = fields.String(data_key="name")

    @post_load
    def load_genre(self, data, **kwargs):
        return Genre(**data)
