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
    session: sessionmaker() = 1
    engine = 1

    def __init__(self, base_path: str):
        self.engine = create_engine('sqlite:///' + base_path+'?check_same_thread=False', echo=True)

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

    def add(self, instance):
        self.session.add(instance)
        self.save()

    def delete(self, instance):
        self.session.delete(instance)
        self.save()

    def save(self):     # TODO realise the save() function
        self.session.commit()
        pass
