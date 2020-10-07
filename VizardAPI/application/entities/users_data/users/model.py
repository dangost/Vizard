from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from application.db.model.orm.base import Base


class User(Base):
    __tablename__ = "Users"

    def __init__(self, user_id=None, name=None, email=None, pass_hash=None, is_admin=None, avatar=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.pass_hash = pass_hash
        self.is_admin = is_admin
        self.avatar = avatar

    user_id = Column("id", Integer, primary_key=True, unique=True)

    name = Column("name", String)

    email = Column("email", String)

    pass_hash = Column("passHash", String)

    is_admin = Column("admin", Boolean)

    avatar = Column("avatar", String)
