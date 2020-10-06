from .model import Studio
from .schema import StudioSchema
from application.app import base


class StudiosRepository:
    @staticmethod
    def get_all_studios():
        return base.studios

    @staticmethod
    def get_id_studio(item_id) -> Studio or str:
        for each in base.studios:
            if each.studio_id == item_id:
                return each
        return "No such Id"

    @staticmethod
    def post_studio(json_data: dict):
        studio = StudioSchema(many=False).load(json_data)
        if type(studio) is not studio:
            return "Invalid data"
        base.studios.append(studio)
        base.save()
        return "OK"

    @staticmethod
    def put_studio(studio_id: int, json_data: dict):
        for i in range(len(base.studios)):
            if base.studios[i].studio_id == studio_id:
                studio = StudioSchema(many=False).load(json_data)
                if type(studio) is Studio:
                    return "Invalid data"
                base.studios[i] = studio
                base.save()
                return "OK"
        return "No such Id"

    @staticmethod
    def delete_studio(item_id: int):
        for each in base.studios:
            if each.studio_id == item_id:
                base.studios.remove(each)
                base.save()
                return "OK"
        return "No such Id"
