from marshmallow import fields, Schema, post_load
from application.entities.studios.model import Studio


class StudiosSchema(Schema):
    studio_id = fields.Integer(data_key="id")

    name = fields.String(data_key="name")

    avatar = fields.String(data_key="avt")

    description = fields.String(data_key="desc")

    @post_load
    def load_studio(self, data, **kwargs):
        return Studio(**data)
