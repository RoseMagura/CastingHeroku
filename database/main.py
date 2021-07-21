import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


load_dotenv()
database_path = os.getenv('DATABASE_URL')

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config.from_object('config')
    migrate = Migrate(app, db)
    db.app = app
    db.init_app(app)
    db.create_all()

