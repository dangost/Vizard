from .model import User
from application.entities.abstract.base_repository import BaseRepository


class UsersRepository(BaseRepository):
    def get_all(self):
        return self.db.users

    def get_id(self, item_id):
        for each in self.db.users:
            if each.user_id == item_id:
                return each
        return "No such Id"

    def find(self, condition):
        res = []
        for each in self.db.users:
            if condition(each):
                res.append(each)
        return res

    def add(self, obj: User):
        for user in self.db.users:
            if obj.email == user.email:
                return "BAD"

        self.db.users.append(obj)
        self.db.add(obj)
        return "OK"

    def replace(self, item, item_id):
        for i in range(len(self.db.users)):
            if self.db.users[i].user_id == item_id:
                late = self.db.users[i]
                self.db.users[i] = item
                self.db.update(item, late)
                return "OK"
        return "No such Id"

    def remove(self, item_id: int):
        for each in self.db.users:
            if each.user_id == item_id:
                self.db.users.remove(each)
                self.db.delete(each)
                return "OK"
        return "No such Id"

    def login_check(self, login):
        for each in self.get_all():
            if each.email == login.email and each.pass_hash == login.pass_hash:
                return {"Id": each.user_id, "Result": "true"}
        return {"Id": -1, "Result": "false"}
