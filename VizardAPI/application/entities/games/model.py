from sqlalchemy import Column, Integer, String, Float, ForeignKey
from application.db.model.orm.base import Base


class Game(Base):
    __tablename__ = "Games"

    def __init__(self, id=None, name=None, avt=None, tr=None, desc=None, os=None, rt=None,
                 prc=None, stdId=None, gnrId=None, stm=None, trr=None, sys=None):
        self.game_id = id
        self.name = name
        self.avatar = avt
        self.description = desc
        self.platform = os
        self.trailer = tr
        self.steam = stm
        self.torrent = trr
        self.rate = rt
        self.price = prc
        self.studio_id = stdId
        self.genre_id = gnrId
        self.system_requirements = sys

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


