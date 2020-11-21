from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from application.db.model.orm.base import Base


class User(Base):
    __tablename__ = "Users"

    def __init__(self, id=None, name=None, email=None, hash=None, adm=None, avt=None):
        self.user_id = id
        self.name = name
        self.email = email
        self.pass_hash = hash
        self.admin_level = adm
        if self.admin_level is None:
            self.admin_level = 0
        self.avatar = avt

    user_id = Column("id", Integer, primary_key=True, unique=True)

    name = Column("name", String)

    email = Column("email", String)

    pass_hash = Column("passHash", String)

    admin_level = Column("admin", Integer)

    avatar = Column("avatar", String)


class UserAuth:
    def __init__(self, email, pass_hash):
        self.email = email
        self.pass_hash = pass_hash
