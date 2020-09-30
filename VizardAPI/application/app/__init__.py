from application.db.abstract.base_database import BaseDatabase
from application.db.model.json_database import JsonDatabase

base_path = r"C:\Users\danil\Desktop\base.zip"

base: BaseDatabase = JsonDatabase(base_path)
