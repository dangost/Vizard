from application.db.abstract.base_database import BaseDatabase
from application.db.model.database import Database

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

base_path = r"C:\Users\danil\Desktop\base.dbf"

engine = create_engine('sqlite:///'+base_path, echo=True)

Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

base: BaseDatabase = Database(base_path)

