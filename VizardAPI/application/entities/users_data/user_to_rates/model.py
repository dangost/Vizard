from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from application.db.model.orm.base import Base


class UserToRates(Base):
    __tablename__ = "UserToRate"

    def __init__(self, id=None, user_id=None, game_id=None, rate=None):
        self.key = id
        self.user_id = user_id
        self.game_id = game_id
        self.rate = rate

    key = Column("id", Integer, primary_key=True, unique=True)

    user_id = Column("userId", Integer, ForeignKey("Users.id"))

    game_id = Column("gameId", Integer, ForeignKey("Games.id"))

    rate = Column("rate", Integer)
