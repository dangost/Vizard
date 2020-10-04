from application.db.model.database import Database
from .model import Game
from application.app import base


class GamesRepository:
    def get_all_games(self):
        return base.games

    def get_id_game(self, item_id):
        for each in base.games:
            if each.id == item_id:
                return each

    def post_game(self, json_data: dict):
        pass

    def delete_game(self, game_id: int):
        pass
