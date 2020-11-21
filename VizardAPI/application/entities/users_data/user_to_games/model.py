from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from application.db.model.orm.base import Base


class UserToGames(Base):
    __tablename__ = "UserToGames"

    def __init__(self, key=None, uid=None, gid=None):
        self.key = key
        self.user_id = uid
        self.game_id = gid

    key = Column("id", Integer, primary_key=True, unique=True)

    user_id = Column("userId", Integer, ForeignKey("Users.id"))

    game_id = Column("gameId", Integer, ForeignKey("Games.id"))
