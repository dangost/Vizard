from .model import UserToGames
from application.entities.abstract.base_repository import BaseRepository


class UserToGamesRepository(BaseRepository):
    def get_all(self):
        return self.db.get_all(UserToGames)

    def get_id(self, item_id):
        user_to_games = self.db.get_by_id(UserToGames, item_id)
        if user_to_games is not None:
            return user_to_games
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
        temp = self.get_id(item_id)
        if temp == "No such Id":
            return temp
        self.db.update(UserToGames, UserToGames.key, item_id, item)
        return "OK"

    def remove(self, item_id: int):
        temp = self.get_id(item_id)
        if temp == "No such Id":
            return temp
        self.db.delete(temp)
        return "OK"
