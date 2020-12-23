from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from application.db.model.orm.base import Base


class User(Base):
    __tablename__ = "Users"

    def __init__(self, id=None, name=None, email=None, pass_hash=None, admin_level=None, avatar=None,
                 telegram=None, steam=None):
        self.user_id = id
        self.name = name
        self.email = email
        self.pass_hash = pass_hash
        self.admin_level = admin_level
        if self.admin_level is None:
            self.admin_level = 0
        self.avatar = avatar
        self.telegram = telegram
        self.steam = steam

    user_id = Column("id", Integer, primary_key=True, unique=True)

    name = Column("name", String(255))

    email = Column("email", String(255))

    pass_hash = Column("passHash", String(255))

    admin_level = Column("admin", Integer)

    avatar = Column("avatar", String(255))

    telegram = Column("telegram", String(255))

    steam = Column("steam", String(255))

    def json(self, id):
        json = {
            "user_id": id,
            "name": self.name,
            "email": self.email,
            "pass_hash": self.pass_hash,
            "admin_level": self.admin_level,
            "avatar": self.avatar,
            "telegram": self.telegram,
            "steam": self.steam
        }
        return json


class UserAuth:
    def __init__(self, email, pass_hash):
        self.email = email
        self.pass_hash = pass_hash
