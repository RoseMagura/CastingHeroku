# from main import db

# '''
# Actor
# Attributes include name, age, and gender
# '''


# class Actor(db.Model):
#     __tablename__ = 'Actors'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     age = db.Column(db.Integer())
#     gender = db.Column(db.String())
#     movies = db.relationship('Movie', secondary=cast,
#                              backref=db.backref('Movies', lazy=True))

#     def __init__(self, name, age, gender, movies):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.movies = movies

#     def insert(self):
#         db.session.add(self)
#         db.session.commit()

#     def update(self):
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()

#     def format(self):
#         return{
#             'id': self.id,
#             'name': self.name,
#             'age': self.age,
#             'gender': self.gender,
#             'movies': [m.name for m in self.movies]
#         }
