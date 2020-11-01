from .model import User
from application.entities.abstract.base_repository import BaseRepository


class UsersRepository(BaseRepository):
    def get_all(self):
        return self.db.users

    def get_id(self, item_id):
        for each in self.db.users:
            if each.id == item_id:
                return each
        return "No such Id"

    def find(self, condition):
        res = []
        for each in self.db.users:
            if condition(each):
                res.append(each)
        return res

    def add(self, obj: User):
        self.db.users_to_rates.append(obj)
        self.db.save()
        return "OK"

    def replace(self, item, item_id):
        for i in range(len(self.db.users)):
            if self.db.users[i].id == item_id:
                self.db.users[i] = item
                self.db.save()
                return "OK"
        return "No such Id"

    def remove(self, item_id: int):
        for each in self.db.users:
            if each.id == item_id:
                self.db.users.remove(each)
                self.db.save()
                return "OK"
        return "No such Id"
