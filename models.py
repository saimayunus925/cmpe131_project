from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def __repr__(self):
        return f'<user:{self.username}>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(256))
    timestamps = db.Column(db.Datetime, index = True, default = datetime.utcnow)
    user_id = (db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<user:{self.username}>'

