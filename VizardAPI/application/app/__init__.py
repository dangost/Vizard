from application.db.abstract.base_database import BaseDatabase
from application.db.model.database import Database

base_path = r"C:\Users\danil\Desktop\base.db"

base: BaseDatabase = Database(base_path)
session = Database.session

