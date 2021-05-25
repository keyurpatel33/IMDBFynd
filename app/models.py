from app.flaskapi import db


#MOVIES
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    popularity = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String(80), nullable=False)
    genre = db.Column(db.String(80), nullable=False)
    imdb_score = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(80), nullable=False)

    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'director': self.director,
            'genre': self.genre.split(','),
            '99popularity': self.popularity,
            'imdb_score': self.imdb_score
        }


#USER
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(500))
    admin = db.Column(db.Boolean)

    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'admin': self.admin
        }