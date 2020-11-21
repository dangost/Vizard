from .model import UserToRates
from application.entities.abstract.base_repository import BaseRepository


class UserToRatesRepository(BaseRepository):
    def get_all(self):
        return self.db.users_to_rates

    def get_id(self, item_id):
        for each in self.db.users_to_rates:
            if each.id == item_id:
                return each
        return "No such Id"

    def find(self, condition):
        res = []
        for each in self.db.users_to_rates:
            if condition(each):
                res.append(each)
        return res

    def add(self, obj: UserToRates):
        self.db.users_to_rates.append(obj)
        self.db.add(obj)
        return "OK"

    def replace(self, item, item_id):
        for i in range(len(self.db.games)):
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
