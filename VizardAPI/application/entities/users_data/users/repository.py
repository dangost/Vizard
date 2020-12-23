from .model import User
from application.entities.abstract.base_repository import BaseRepository


class UsersRepository(BaseRepository):
    def get_all(self):
        return self.db.get_all(User)

    def get_id(self, item_id):
        users = self.db.get_by_id(User, item_id)
        if users is not None:
            return users
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
        temp = self.get_id(item_id)
        if temp == "No such Id":
            return temp
        self.db.update(User, User.user_id, item_id, item)
        return "OK"

    def remove(self, item_id: int):
        temp = self.get_id(item_id)
        if temp == "No such Id":
            return temp
        self.db.delete(temp)
        return "OK"

    def login_check(self, login):
        for each in self.get_all():
            if each.email == login.email and each.pass_hash == login.pass_hash:
                return {"Id": each.user_id, "Result": "true"}
        return {"Id": -1, "Result": "false"}
