from sqlalchemy import String, Integer, Column
from application.db.model.orm.base import Base


class Studio(Base):
    __tablename__ = "Studios"

    def __init__(self, id=None, name=None, avt=None, desc=None):
        self.studio_id = id
        self.name = name
        self.avatar = avt
        self.description = desc

    studio_id = Column("id", Integer, primary_key=True, unique=True)

    name = Column("name", String)

    avatar = Column("avatar", String)

    description = Column("description", String)

    def to_dict(self):
        data = {'id': self.studio_id,
                'name': self.name,
                'avatar': self.description}
        return data
