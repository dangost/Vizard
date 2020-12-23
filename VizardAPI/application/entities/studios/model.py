from sqlalchemy import String, Integer, Column
from application.db.model.orm.base import Base


class Studio(Base):
    __tablename__ = "Studios"

    def __init__(self, studio_id=None, name=None, avatar=None, description=None):
        self.studio_id = studio_id
        self.name = name
        self.avatar = avatar
        self.description = description

    studio_id = Column("id", Integer, primary_key=True, unique=True)

    name = Column("name", String(255))

    avatar = Column("avatar", String(255))

    description = Column("description", String(255))

    def json(self, id):
        json = {
            "studio_id": id,
            "name": self.name,
            "avatar": self.avatar, "description": self.description
        }
        return json
