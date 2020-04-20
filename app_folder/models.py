from app_folder import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def __repr__(self):
        """ Build in function to modify

        Returns:
            print variable in string

        Changelog:
            4/19 Ali
            
        """
        
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        """ Build in function to modify

        Returns:
            print variable in string

        Changelog:
            4/19 Ali

        """
        return '<Posts {}>'.format(self.body)
