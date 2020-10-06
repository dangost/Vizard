from marshmallow import fields, Schema, post_load
from application.entities.studios.model import Studio


class StudioSchema(Schema):
    studio_id = fields.Integer(data_key="id", required=False)

    name = fields.String(data_key="name", required=True)

    avatar = fields.String(data_key="avt", required=False)

    description = fields.String(data_key="desc", required=True)

    @post_load
    def load_studio(self, data, **kwargs):
        return Studio(**data)
