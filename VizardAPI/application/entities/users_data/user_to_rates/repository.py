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
        self.db.save()
        return "OK"

    def replace(self, item, item_id):
        for i in range(len(self.db.games)):
            if self.db.users_to_rates[i].id == item_id:
                self.db.users_to_rates[i] = item
                self.db.save()
                return "OK"
        return "No such Id"

    def remove(self, item_id: int):
        for each in self.db.users_to_rates:
            if each.id == item_id:
                self.db.users_to_rates.remove(each)
                self.db.save()
                return "OK"
        return "No such Id"
