from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from application.db.model.orm.base import Base


class User(Base):
    __tablename__ = "Users"

    def __init__(self, user_id=None, name=None, email=None, pass_hash=None, is_admin=None, avatar=None):
        self.user_id = user_id
        self.name = name
        self.pass_hash = pass_hash
        self.is_admin = is_admin
        self.avatar = avatar

    user_id = Column("id", Integer, primary_key=True, unique=True)

    name = Column("name", String)

    email = Column("email", String)

    pass_hash = Column("passHash", String)

    is_admin = Column("admin", Boolean)

    avatar = Column("avatar", String)


class UserToGames(Base):
    __tablename__ = "UserToGames"

    def __init__(self, key=None, user_id=None, game_id=None):
        self.key = key
        self.user_id = user_id
        self.game_id = game_id

    key = Column("id", Integer, primary_key=True, unique=True)

    user_id = Column("userId", Integer, ForeignKey("User.id"))

    game_id = Column("gameId", Integer, ForeignKey("Games.id"))


class UserToRate(Base):
    __tablename__ = "UserToRate"

    def __init__(self, key=None, user_id=None, game_id=None, rate=None):
        self.key = key
        self.user_id = user_id
        self.game_id = game_id
        self.rate = rate

    key = Column("id", Integer, primary_key=True, unique=True)

    user_id = Column("userId", Integer, ForeignKey("User.id"))

    game_id = Column("gameId", Integer, ForeignKey("Games.id"))

    rate = Column("rate", Integer)
