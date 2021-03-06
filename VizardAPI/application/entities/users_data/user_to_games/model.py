from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from application.db.model.orm.base import Base


class UserToGames(Base):
    __tablename__ = "UserToGames"

    def __init__(self, id=None, user_id=None, game_id=None):
        self.key = id
        self.user_id = user_id
        self.game_id = game_id

    key = Column("id", Integer, primary_key=True, unique=True)

    user_id = Column("userId", Integer, ForeignKey("Users.id"))

    game_id = Column("gameId", Integer, ForeignKey("Games.id"))

    def json(self, id):
        json = {
            "key": id,
            "user_id": self.user_id,
            "game_id": self.game_id
        }
        return json
