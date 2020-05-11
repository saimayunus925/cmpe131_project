from app_folder import db
import datetime


class User(db.Model):
    """ Build in function to modify

        Returns:
            print variable in string

        Changelog:
            4/19 Ali
            
            5/3 Dylan: Added events relationship
            5/10 Dylan: Added salt
        """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    salt = db.Column(db.String(32))
    password_hash = db.Column(db.String(256), default = 'fatal-error')
    start_time = db.Column(db.Time, default=datetime.time(9, 0))
    end_time = db.Column(db.Time, default=datetime.time(22, 0))
    meeting_length = db.Column(db.Integer, default=30)


    events = db.relationship('Event', backref='creator', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.username)


class Event(db.Model):
    '''
    Event database
    @id unique id required for database
    @user_id user's id that the event is for
    @datetime date and time of the meeting
    @guest_name name input by the person requesting the meeting
    @description description of the meeting

    Changelog:
        5/3 Dylan: Initial Implementation
    '''

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    datetime = db.Column(db.DateTime(), index=True)
    guest_name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(256), default = '')

    def __repr(self):
        return f'<Datetime: {datetime}, Guest: {guest_name}>'