from .model import UserToGames
from .schema import UserToGamesSchema


class UserToGamesRepository:
    def __init__(self, base):
        self.db = base

    def get_all_utd(self):
        return self.db.users_to_games

    def get_id_utd(self, item_id) -> UserToGames or str:
        for each in self.db.users_to_games:
            if each.id == item_id:
                return each
        return "No such Id"

    def post_utd(self, json_data: dict):
        utd = UserToGamesSchema(many=False).load(json_data)
        if type(utd) is not UserToGames:
            return "Invalid data"
        self.db.users_to_games.append(utd)
        self.db.save()
        return "OK"

    def put_utd(self, utd_id: int, json_data: dict):
        for i in range(len(self.db.games)):
            if self.db.users_to_games[i].id == utd_id:
                utd = UserToGamesSchema(many=False).load(json_data)
                if type(utd) is UserToGames:
                    return "Invalid data"
                self.db.users_to_games[i] = utd
                self.db.save()
                return "OK"
        return "No such Id"

    def delete_utd(self, utd_id: int):
        for each in self.db.users_to_games:
            if each.utd_id == utd_id:
                self.db.users_to_games.remove(each)
                self.db.save()
                return "OK"
        return "No such Id"
