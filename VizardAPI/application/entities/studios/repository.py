from .model import Studio
from .schema import StudioSchema


class StudiosRepository:
    def __init__(self, base):
        self.db = base

    def get_all_studios(self):
        return self.db.studios

    def get_id_studio(self, item_id) -> Studio or str:
        for each in self.db.studios:
            if each.studio_id == item_id:
                return each
        return "No such Id"

    def post_studio(self, json_data: dict):
        studio = StudioSchema(many=False).load(json_data)
        if type(studio) is not studio:
            return "Invalid data"
        self.db.studios.append(studio)
        self.db.save()
        return "OK"

    def put_studio(self, studio_id: int, json_data: dict):
        for i in range(len(self.db.studios)):
            if self.db.studios[i].studio_id == studio_id:
                studio = StudioSchema(many=False).load(json_data)
                if type(studio) is Studio:
                    return "Invalid data"
                self.db.studios[i] = studio
                self.db.save()
                return "OK"
        return "No such Id"

    def delete_studio(self, item_id: int):
        for each in self.db.studios:
            if each.studio_id == item_id:
                self.db.studios.remove(each)
                self.db.save()
                return "OK"
        return "No such Id"
