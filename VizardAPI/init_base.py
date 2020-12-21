from application.db.abstract.base_database import BaseDatabase
from application.db.model.database import Database


def create_base():
    base_path = "base.db"

    base: BaseDatabase = Database(base_path)
    session = Database.session

    return base, session
