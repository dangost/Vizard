from application.app.config import base_path
from application.db.abstract.base_database import BaseDatabase
from application.db.model.database import Database


base: BaseDatabase = Database(base_path)
session = Database.session
