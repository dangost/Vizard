from application.db.abstract.base_database import BaseDatabase
from application.entities.games.schema import Game
from application.entities.genres.schema import Genre
from application.entities.studios.schema import Studio
from zipfile import ZipFile
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from application.db.model.orm.base import Base


class Database(BaseDatabase):
    session: sessionmaker()

    # games_path: str = "games.json"
    # studios_path: str = "studios.json"
    # genres_path: str = "genres.json"

    engine = 1

    def __init__(self, base_path: str):
        self.engine = create_engine('sqlite:///' + base_path, echo=True)

    def load(self):
        Base.metadata.create_all(self.engine)
        _session = sessionmaker()
        _session.configure(bind=self.engine)
        self.session = _session()

        self.initialize()

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

    def initialize(self):
        genre = Genre("Action", "Description")
        studio = Studio("Rockstar Game", "avatar", "description")
        game = Game("name", "avarat", "trailer", "description", "android", "steam", "torrent", 9.0, 10.0, 0, 0, "pent")

        self.session.add(genre)
        self.session.add(game)
        self.session.commit()
