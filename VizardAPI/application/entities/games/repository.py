from .model import Game
from .schema import GameSchema


class GamesRepository:
    def __init__(self, base):
        self.db = base

    def get_all_games(self):
        return self.db.games

    def get_id_game(self, item_id) -> Game or str:
        for each in self.db.games:
            if each.game_id == item_id:
                return each
        return "No such Id"

    def post_game(self, json_data: dict):
        game = GameSchema(many=False).load(json_data)
        if type(game) is not Game:
            return "Invalid data"
        self.db.games.append(game)
        self.db.save()
        return "OK"

    def put_game(self, game_id: int, json_data: dict):
        for i in range(len(self.db.games)):
            if self.db.games[i].game_id == game_id:
                game = GameSchema(many=False).load(json_data)
                if type(game) is Game:
                    return "Invalid data"
                self.db.games[i] = game
                self.db.save()
                return "OK"
        return "No such Id"

    def delete_game(self, game_id: int):
        for each in self.db.games:
            if each.game_id == game_id:
                self.db.games.remove(each)
                self.db.save()
                return "OK"
        return "No such Id"
