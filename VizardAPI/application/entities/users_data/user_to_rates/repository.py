from .model import UserToRates
from .schema import UserToRatesSchema
from typing import List
from application.entities.games.model import Game


class UserToRatesRepository:
    def __init__(self, base):
        self.db = base

    def get_all_utr(self):
        return self.db.users_to_rates

    def get_id_utr(self, item_id) -> UserToRates or str:
        for each in self.db.users_to_rates:
            if each.id == item_id:
                return each
        return "No such Id"

    def get_user_games(self, user_id) -> List[Game]:
        games = []

        for each in self.db.users_to_rates:
            if each.user_id == user_id:
                for such in self.db.games:
                    if such.game_id == each.game_id:
                        games.append(such)
        return games

    def post_utr(self, json_data: dict):
        utr = UserToRatesSchema(many=False).load(json_data)
        if type(utr) is not UserToRates:
            return "Invalid data"
        self.db.users_to_rates.append(utr)
        self.db.save()
        return "OK"

    def put_utr(self, utr_id: int, json_data: dict):
        for i in range(len(self.db.users_to_rates)):
            if self.db.users_to_rates[i].id == utr_id:
                utr = UserToRatesSchema(many=False).load(json_data)
                if type(utr) is UserToRates:
                    return "Invalid data"
                self.db.users_to_rates[i] = utr
                self.db.save()
                return "OK"
        return "No such Id"

    def delete_utr(self, utr_id: int):
        for each in self.db.users_to_rates:
            if each.id == utr_id:
                self.db.users_to_rates.remove(each)
                self.db.save()
                return "OK"
        return "No such Id"
