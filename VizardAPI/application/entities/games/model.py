from sqlalchemy import Column, Integer, String, Float, ForeignKey
from application.db.model.orm.base import Base


class Game(Base):
    __tablename__ = "Games"

    def __init__(self, id=None, name=None, avatar=None, trailer=None, description=None, platform=None, rate=None,
                 price=None, studio_id=None, genre_id=None, steam=None, torrent=None, system_requirements=None):
        self.game_id = id
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


