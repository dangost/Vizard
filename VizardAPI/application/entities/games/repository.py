from .model import Game
from application.entities.abstract.base_repository import BaseRepository


class GamesRepository(BaseRepository):
    def get_all(self):
        return self.db.get_all(Game)

    def get_id(self, item_id) -> Game or str:
        game = self.db.get_by_id(Game, item_id)
        if game is not None:
            return game
        return "No such Id"

    def find(self, condition):
        res = []
        for each in self.get_all():
            if condition(each):
                res.append(each)
        return res

    def add(self, game: Game):
        self.db.games.append(game)
        self.db.add(game)
        return "OK"

    def replace(self, game: Game, game_id: int):
        temp = self.get_id(game_id)
        if temp == "No such Id":
            return temp
        self.db.update(Game, Game.game_id, game_id, game)
        return "OK"

    def remove(self, game_id: int):
        temp = self.get_id(game_id)
        if temp == "No such Id":
            return temp
        self.db.delete(temp)
        return "OK"
