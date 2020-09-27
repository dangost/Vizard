from application.db.abstract.base_database import BaseDatabase
from application.entities.games.schema import GamesSchema
from application.entities.genres.schema import GenresSchema
from application.entities.studios.schema import StudiosSchema
from zipfile import ZipFile
import json


class JsonDatabase(BaseDatabase):
    base: ZipFile

    def __init__(self, base_path: str):
        try:
            self.base = ZipFile(base_path, 'r')

        except FileExistsError:
            self.create_base(base_path)

    def load(self):
        games_json: dict = json.load(self.base.open(self.games_path))
        studios_json: dict = json.load(self.base.open(self.studios_path))
        genres_json: dict = json.load(self.base.open(self.genres_path))

        # serializing to lists
        temp = []

        for each in games_json:
            temp.append(GamesSchema.load_game(each))

        self.games = temp
        temp = []

        for each in studios_json:
            temp.append(StudiosSchema.load_studio(each))
        self.studios = temp
        temp = []

        for each in genres_json:
            temp.append(GenresSchema.load_genre(each))
        self.genres = temp
        temp = []
        del temp

    def save(self):
        pass

    def create_base(self, path: str):
        base = ZipFile(path, 'w')

        base.write(self.games_path)
        base.write(self.studios_path)
        base.write(self.genres_path)
