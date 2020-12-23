from sqlalchemy import Column, String, Integer
from application.db.model.orm.base import Base


class Genre(Base):
    __tablename__ = "Genres"

    def __init__(self, genre_id=None, name=None, description=None):
        self.genre_id = genre_id
        self.name = name
        self.description = description

    genre_id = Column("id", Integer, primary_key=True, unique=True)

    name = Column("name", String(255))

    description = Column("description", String(255))

    def json(self, id):
        json = {
            "genre_id": id,
            "name": self.name,
            "description": self.description
        }
        return json
