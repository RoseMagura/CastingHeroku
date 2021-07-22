from CastingHeroku.extensions import db
'''
Actor
Attributes include name, age, and gender
'''
cast = db.Table('cast',
                db.Column('actor_id',
                          db.Integer, db.ForeignKey('actors.id'),
                          primary_key=True),
                db.Column('movie_id',
                          db.Integer, db.ForeignKey('movies.id'),
                          primary_key=True))


class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    gender = db.Column(db.String())
    movies = db.relationship('Movie', secondary=cast,
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


'''
Movie
Attributes include title and release date
'''


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String())
    release_date = db.Column(db.Integer)
    actors = db.relationship('Actor', secondary=cast)

    def __init__(self, name, release_date, actors):
        self.name = name
        self.release_date = release_date
        self.actors = actors

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'name': self.name,
            'release_date': self.release_date,
            'actors': [a.name for a in self.actors]
        }
