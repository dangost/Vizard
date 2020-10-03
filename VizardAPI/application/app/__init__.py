from application.db.abstract.base_database import BaseDatabase
from application.db.model.database import JsonDatabase

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

base_path = r"C:\Users\danil\Desktop\base.db"

engine = create_engine('sqlite:///'+base_path, echo=True)

Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

base: BaseDatabase = JsonDatabase(base_path)

