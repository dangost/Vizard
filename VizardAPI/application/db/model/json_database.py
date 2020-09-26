from application.db.abstract.base_database import BaseDatabase
from zipfile import ZipFile
import json


class JsonDatabase(BaseDatabase):
    base: ZipFile

    def __init__(self, base_path: str):
        try:
            self.base = ZipFile(base_path, 'r')

            pass
        except FileExistsError:
            self.create_base()
            pass
        pass

    def load(self):
        games_json: dict = json.load(self.base.open(self.games_path))
        studios_json: dict = json.load(self.base.open(self.studios_path))
        genres_json: dict = json.load(self.base.open(self.genres_path))

    def save(self):
        pass

    def create_base(self):
        pass
