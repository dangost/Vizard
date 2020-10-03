from sqlalchemy import Column, String, Integer
from application.db.model.orm.base import Base


class Genre(Base):
    __tablename__ = "Games"

    def __init__(self, genre_id, name, description):
        self.genre_id = genre_id
        self.name = name
        self.description = description

    genre_id = Column("id", Integer, primary_key=True)

    name = Column("name", String)

    description = Column("description", String)
