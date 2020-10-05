from .model import Game
from .schema import GamesSchema
from application.app import base


class GamesRepository:
    @staticmethod
    def get_all_games():
        return base.games

    @staticmethod
    def get_id_game(item_id) -> Game or str:
        for each in base.games:
            if each.game_id == item_id:
                return each
        return "No such Id"

    @staticmethod
    def post_game(json_data: dict):
        game = GamesSchema(many=False).load(json_data)
        if type(game) is not Game:
            return "Invalid data"
        base.games.append(game)
        base.save()
        return "OK"

    @staticmethod
    def put_game(game_id: int, json_data: dict):
        for i in range(len(base.games)):
            if base.games[i].game_id == game_id:
                game = GamesSchema(many=False).load(json_data)
                if type(game) is Game:
                    return "Invalid data"
                base.games[i] = game
                base.save()
                return "OK"
        return "No such Id"

    @staticmethod
    def delete_game(game_id: int):
        for each in base.games:
            if each.game_id == game_id:
                base.games.remove(each)
                base.save()
                return "OK"
        return "No such Id"
