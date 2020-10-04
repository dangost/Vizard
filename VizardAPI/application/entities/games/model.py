from sqlalchemy import Column, Integer, String, Float, ForeignKey
from application.db.model.orm.base import Base


class Game(Base):
    __tablename__ = "Games"

    def __init__(self, name, avatar, trailer, description, platform, steam, torrent, rate,
                 price, studio_id, genre_id, system_requirements, game_id=None):
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

    name = Column("name", String)

    avatar = Column("avatar", String)  # picture link

    trailer = Column("trailer", String)  # yt link

    description = Column("description", String)

    platform = Column("platform", String)

    steam = Column("steam", String)  # steam link

    torrent = Column("torrent", String)  # torrent link

    rate = Column("rate", Float)

    price = Column("price", Float)

    studio_id = Column("studioId", Integer, ForeignKey("Studios.id"))

    genre_id = Column("genreId", Integer, ForeignKey("Genres.id"))

    system_requirements = Column("systemReq", String)
