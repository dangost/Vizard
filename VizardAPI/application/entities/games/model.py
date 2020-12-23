from sqlalchemy import Column, Integer, String, Float, ForeignKey
from application.db.model.orm.base import Base


class Game(Base):
    __tablename__ = "Games"

    def __init__(self, game_id=None, name=None, avatar=None, trailer=None, description=None, platform=None, rate=None,
                 price=None, studio_id=None, genre_id=None, steam=None, torrent=None, system_requirements=None):
        self.game_id = game_id
        self.name = name
        self.avatar = avatar
        self.description = description
        self.platform = platform
        self.trailer = trailer
        self.steam = steam
        self.torrent = torrent
        self.rate = rate
        self.price = price
        self.studio_id = studio_id
        self.genre_id = genre_id
        self.system_requirements = system_requirements

    game_id = Column("id", Integer, primary_key=True, unique=True)

    name = Column("name", String(255))

    avatar = Column("avatar", String(255))  # picture link

    trailer = Column("trailer", String(255))  # yt link

    description = Column("description", String(255))

    platform = Column("platform", String(255))

    steam = Column("steam", String(255))  # steam link

    torrent = Column("torrent", String(255))  # torrent link

    rate = Column("rate", Float)

    price = Column("price", Float)

    studio_id = Column("studioId", Integer, ForeignKey("Studios.id"))

    genre_id = Column("genreId", Integer, ForeignKey("Genres.id"))

    system_requirements = Column("systemReq", String(255))

    def json(self, id):
        json = {
            "game_id": id,
            "name": self.name,
            "avatar": self.avatar,
            "trailer": self.trailer,
            "description": self.description,
            "steam": self.steam,
            "platform": self.platform,
            "torrent": self.torrent,
            "rate": self.rate,
            "price": self.price,
            "studio_id": self.studio_id,
            "genre_id": self.genre_id,
            "system_requirements": self.system_requirements
        }
        return json


