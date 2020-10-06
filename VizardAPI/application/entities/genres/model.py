from sqlalchemy import Column, String, Integer
from application.db.model.orm.base import Base


class Genre(Base):
    __tablename__ = "Genres"

    def __init__(self, name=None, description=None, genre_id=None):
        self.genre_id = genre_id
        self.name = name
        self.description = description

    genre_id = Column("id", Integer, primary_key=True, unique=True)

    name = Column("name", String)

    description = Column("description", String)
