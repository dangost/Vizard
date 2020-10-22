from .model import Studio
from application.entities.abstract.base_repository import BaseRepository


class StudiosRepository(BaseRepository):
    def get_all(self):
        return self.db.studios

    def get_id(self, item_id):
        for each in self.db.studios:
            if each.studio_id == item_id:
                return each
        return "No such Id"

    def find(self, condition):
        res = []
        for each in self.db.studios:
            if condition(each):
                res.append(each)
        return res

    def add(self, studio: Studio):
        self.db.studios.append(studio)
        self.db.save()
        return "OK"

    def replace(self, studio, studio_id):
        for i in range(len(self.db.studios)):
            if self.db.studios[i].studio_id == studio_id:
                self.db.studios[i] = studio
                self.db.save()
                return "OK"
        return "No such Id"

    def remove(self, studio_id: int):
        for each in self.db.studios:
            if each.studio_id == studio_id:
                self.db.studios.remove(each)
                self.db.save()
                return "OK"
        return "No such Id"
