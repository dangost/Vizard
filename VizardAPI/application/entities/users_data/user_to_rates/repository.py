from .model import UserToRates
from application.entities.abstract.base_repository import BaseRepository


class UserToRatesRepository(BaseRepository):
    def get_all(self):
        return self.db.get_all(UserToRates)

    def get_id(self, item_id):
        user_to_rates = self.db.get_by_id(UserToRates, item_id)
        if user_to_rates is not None:
            return user_to_rates
        return "No such Id"

    def find(self, condition):
        res = []
        for each in self.get_all():
            if condition(each):
                res.append(each)
        return res

    def add(self, obj: UserToRates):
        self.db.users_to_rates.append(obj)
        self.db.add(obj)
        return "OK"

    def replace(self, item, item_id):
        for i in range(len(self.get_all())):
            if self.db.users_to_rates[i].key == item_id:
                late = self.db.users_to_rates[i]
                self.db.users_to_rates[i] = item
                self.db.update(item, late)
                return "OK"
        return "No such Id"

    def remove(self, item_id: int):
        for each in self.db.users_to_rates:
            if each.key == item_id:
                self.db.users_to_rates.remove(each)
                self.db.delete(each)
                return "OK"
        return "No such Id"
