from application.db.abstract.base_database import BaseDatabase
from application.entities.games.schema import GamesSchema
from application.entities.genres.schema import GenresSchema
from application.entities.studios.schema import StudiosSchema
from zipfile import ZipFile
import json


class JsonDatabase(BaseDatabase):
    base: ZipFile

    games_path: str = "games.json"
    studios_path: str = "studios.json"
    genres_path: str = "genres.json"

    def __init__(self, base_path: str):
        try:
            self.base = ZipFile(base_path, 'r')

        except FileNotFoundError:
            self.create_base(base_path)

    def load(self):
        games_json: dict = json.load(self.base.open(self.games_path))
        studios_json: dict = json.load(self.base.open(self.studios_path))
        genres_json: dict = json.load(self.base.open(self.genres_path))

        # deserializing

        self.games = GamesSchema(many=True).load(games_json)

        self.studios = StudiosSchema(many=True).load(studios_json)

        self.genres = StudiosSchema(many=True).load(genres_json)

    def save(self):
        pass

    def create_base(self, path: str):
        base = ZipFile(path, 'w')

        base.write(self.games_path)
        base.write(self.studios_path)
        base.write(self.genres_path)
        base.close()
