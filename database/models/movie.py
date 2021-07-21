# '''
# Movie
# Attributes include title and release date
# '''


# class Movie(db.Model):
#     __tablename__ = 'Movies'

#     id = db.Column(db.Integer, primary_key=True, unique=True)
#     name = db.Column(db.String())
#     release_date = db.Column(db.Integer)
#     actors = db.relationship('Actor', secondary=cast,
#                              backref=db.backref('Actors', lazy=True))

#     def __init__(self, name, release_date, actors):
#         self.name = name
#         self.release_date = release_date
#         self.actors = actors

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
#             'release_date': self.release_date,
#             'actors': [a.name for a in self.actors]
#         }