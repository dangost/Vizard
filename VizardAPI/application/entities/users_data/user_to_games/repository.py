from .model import UserToGames
from application.entities.abstract.base_repository import BaseRepository


class UserToGamesRepository(BaseRepository):
    def get_all(self):
        return self.db.users_to_games

    def get_id(self, item_id):
        for each in self.db.users_to_games:
            if each.id == item_id:
                return each
        return "No such Id"

    def find(self, condition):
        res = []
        for each in self.db.users_to_games:
            if condition(each):
                res.append(each)
        return res

    def get_user_games(self, user_id):
        games = []

        for each in self.db.users_to_rates:
            if each.user_id == user_id:
                for such in self.db.games:
                    if such.game_id == each.game_id:
                        games.append(such)
        return games

    def add(self, obj: UserToGames):
        self.db.users_to_games.append(obj)
        self.db.add(obj)
        return "OK"

    def replace(self, item, item_id):
        for i in range(len(self.db.games)):
            if self.db.users_to_games[i].key == item_id:
                late = self.db.users_to_games[i]
                self.db.users_to_games[i] = item
                self.db.update(item, late)
                return "OK"
        return "No such Id"

    def remove(self, item_id: int):
        for each in self.db.users_to_games:
            if each.key == item_id:
                self.db.users_to_games.remove(each)
                self.db.delete(each)
                return "OK"
        return "No such Id"
