import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True 

SQLALCHEMY_DATABASE_URI = 'postgres://rnepqcnlixmwvi:2519bee575c528c54829da9d1a171580b5ead791b3fd4b7e7507608c3e8c7354@ec2-52-72-65-76.compute-1.amazonaws.com:5432/dc4mc4boljurn4'
SQLALCHEMY_TRACK_MODIFICATIONS = False