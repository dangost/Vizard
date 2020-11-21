from .model import Game
from application.entities.abstract.base_repository import BaseRepository


class GamesRepository(BaseRepository):
    def get_all(self):
        return self.db.games

    def get_id(self, item_id) -> Game or str:
        for each in self.db.games:
            if each.game_id == item_id:
                return each
        return "No such Id"

    def find(self, condition):
        res = []
        for each in self.db.games:
            if condition(each):
                res.append(each)
        return res

    def add(self, game: Game):
        self.db.games.append(game)
        self.db.add(game)
        return "OK"

    def replace(self, game: Game, game_id: int):
        for i in range(len(self.db.games)):
            if self.db.games[i].game_id == game_id:
                late = self.db.games[i]
                self.db.games[i] = game
                self.db.replace(game, late)
                return "OK"
        return "No such Id"

    def remove(self, game_id: int):
        for each in self.db.games:
            if each.game_id == game_id:
                self.db.games.remove(each)
                self.db.delete(each)
                return "OK"
        return "No such Id"
