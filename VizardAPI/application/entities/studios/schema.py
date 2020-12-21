from marshmallow import fields, Schema, post_load
from application.entities.studios.model import Studio
from application import data_to_snake


class StudioSchema(Schema):
    studio_id = fields.Integer(data_key="Id", required=False)

    name = fields.String(data_key="Name", required=True)

    avatar = fields.String(data_key="Avatar", required=False)

    description = fields.String(data_key="Description", required=True)

    @post_load
    def load_studio(self, data, **kwargs):
        return Studio(**data_to_snake(data))
