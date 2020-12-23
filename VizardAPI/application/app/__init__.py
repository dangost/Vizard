from application.db.abstract.base_database import BaseDatabase
from application.db.model.database import Database

base_path = "mysql+pymysql://gp4i9swtx70muwjd:xku833rhtcddxint@dt3bgg3gu6nqye5f.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/c2sh00xf3siwunr5"

base: BaseDatabase = Database(base_path)
session = Database.session
