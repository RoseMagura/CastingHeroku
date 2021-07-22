from extensions import db
import sys
sys.path.append('...')

cast = db.Table('cast',
                db.Column('actor_id',
                          db.Integer, db.ForeignKey('actors.id'),
                          primary_key=True),
                db.Column('movie_id',
                          db.Integer, db.ForeignKey('movies.id'),
                          primary_key=True))
