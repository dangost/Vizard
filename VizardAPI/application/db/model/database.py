from application.db.abstract.base_database import BaseDatabase
from application.entities.games.schema import GamesSchema, Game
from application.entities.genres.schema import GenresSchema, Genre
from application.entities.studios.schema import StudiosSchema, Studio
from zipfile import ZipFile
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from application.db.model.orm.base import Base


class JsonDatabase(BaseDatabase):
    session: sessionmaker()

    games_path: str = "games.json"
    studios_path: str = "studios.json"
    genres_path: str = "genres.json"

    engine: create_engine()

    def __init__(self, base_path: str):
        self.engine = create_engine('sqlite:///' + base_path, echo=True)

    def load(self):
        Base.metadata.create_all(self.engine)
        _session = sessionmaker()
        _session.configure(bind=self.engine)
        session = _session()

        # games_json: dict = json.load(self.base.open(self.games_path))
        # studios_json: dict = json.load(self.base.open(self.studios_path))
        # genres_json: dict = json.load(self.base.open(self.genres_path))

        # deserializing

        self.games = self.session.query(Game).all()

        self.studios = self.session.query(Studio).all()

        self.genres = self.session.query(Genre).all()

    def save(self):
        self.session.query(Game).delete()
        self.session.query(Studio).delete()
        self.session.query(Genre).delete()

        self.session.query(Game).add_all(self.games)
        self.session.query(Studio).add_all(self.studios)
        self.session.query(Genre).add_all(self.genres)

        self.session.commit()
