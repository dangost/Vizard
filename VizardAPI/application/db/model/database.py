from application.db.abstract.base_database import BaseDatabase
from application.entities.games.schema import Game
from application.entities.genres.schema import Genre
from application.entities.studios.schema import Studio
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from application.db.model.orm.base import Base


class Database(BaseDatabase):
    session: sessionmaker()
    engine = 1

    def __init__(self, base_path: str):
        self.engine = create_engine('sqlite:///' + base_path, echo=True)

    def load(self):
        Base.metadata.create_all(self.engine)
        _session = sessionmaker()
        _session.configure(bind=self.engine)
        self.session = _session()

        self.games = self.session.query(Game).all()
        self.studios = self.session.query(Studio).all()
        self.genres = self.session.query(Genre).all()

    def save(self):     # TODO realise the save() function
        for each in self.games:
            self.session.delete(each)

        for each in self.games:
            self.session.delete(each)

        for each in self.games:
            self.session.delete(each)

        self.session.add_all(self.genres)
        self.session.add_all(self.studios)
        self.session.add_all(self.games)
        self.session.commit()
