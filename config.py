import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
