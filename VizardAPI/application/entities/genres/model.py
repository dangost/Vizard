from sqlalchemy import Column, String, Integer
from application.db.model.orm.base import Base


class Genre(Base):
    __tablename__ = "Genres"

    def __init__(self, id=None, name=None, desc=None):
        self.genre_id = id
        self.name = name
        self.description = desc

    genre_id = Column("id", Integer, primary_key=True, unique=True)

    name = Column("name", String)

    description = Column("description", String)
