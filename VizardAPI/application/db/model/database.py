from application.db.abstract.base_database import BaseDatabase
from application.entities.games.schema import Game
from application.entities.genres.schema import Genre
from application.entities.studios.schema import Studio
from application.entities.users_data.users.schema import User
from application.entities.users_data.user_to_games.schema import UserToGames
from application.entities.users_data.user_to_rates.schema import UserToRates
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
        self.users = self.session.query(User).all()
        self.users_to_games = self.session.query(UserToGames).all()
        self.users_to_rates = self.session.query(UserToRates).all()

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
