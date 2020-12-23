from .model import Studio
from application.entities.abstract.base_repository import BaseRepository
from ..games.model import Game


class StudiosRepository(BaseRepository):
    def get_all(self):
        studios = self.db.get_all(Studio)
        return studios

    def get_id(self, item_id):
        studio = self.db.get_by_id(Studio, item_id)
        if studio is not None:
            return studio
        return "No such Id"

    def get_studio_games(self, studio_id):
        studio_games = []
        games = self.db.get_all(Game)
        for game in games:
            if game.studio_id == studio_id:
                studio_games.append(game)
        return studio_games

    def find(self, condition):
        res = []
        for each in self.db.studios:
            if condition(each):
                res.append(each)
        return res

    def add(self, studio: Studio):
        self.db.add(studio)
        self.db.studios.append(studio)
        return "OK"

    def replace(self, studio, studio_id):
        temp = self.get_id(studio_id)
        if temp == "No such Id":
            return temp
        self.db.update(Studio, Studio.studio_id, studio_id, studio)
        return "OK"

    def remove(self, studio_id: int):
        temp = self.get_id(studio_id)
        if temp == "No such Id":
            return temp
        self.db.delete(temp)
        return "OK"
