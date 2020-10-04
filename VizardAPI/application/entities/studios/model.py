from sqlalchemy import String, Integer, Column
from application.db.model.orm.base import Base


class Studio(Base):
    __tablename__ = "Studios"

    def __init__(self, name, avatar, description, studio_id=None):
        self.studio_id = studio_id
        self.name = name
        self.avatar = avatar
        self.description = description

    studio_id = Column("id", Integer, primary_key=True, unique=True)

    name = Column("name", String)

    avatar = Column("avatar", String)

    description = Column("description", String)
