from application.db.abstract.base_database import BaseDatabase
import zipfile


class JsonDatabase(BaseDatabase):
    base: zipfile

    def __init__(self, base_path: str):
        try:
            self.base = open(base_path)
            pass
        except FileExistsError:
            self.create_base()
            pass
        pass

    def load(self):
        pass

    def save(self):
        pass

    def create_base(self):
        pass
