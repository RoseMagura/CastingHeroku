from database.models.cast import cast
from extensions import db
import sys
sys.path.append('...')
'''
Actor
Attributes include name, age, and gender
'''


class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    gender = db.Column(db.String())
    movies = db.relationship('movie', secondary=cast,
                             backref=db.backref('movies', lazy=True))

    def __init__(self, name, age, gender, movies):
        self.name = name
        self.age = age
        self.gender = gender
        self.movies = movies

    def insert(self):
        try:
            db.session.add(self)
        except Exception as e:
            print(e)
            db.session.rollback()
        finally:
            db.session.commit()

    def update(self):
        # try:
        # db.sessio
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movies': [m.name for m in self.movies]
        }
