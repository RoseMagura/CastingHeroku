import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
database_path = os.getenv('DATABASE_URL')
