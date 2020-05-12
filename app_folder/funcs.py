import hashlib
import os
from app_folder import db
from app_folder.models import User, Event
import datetime

def createNewPswd(user, pswd):
    '''


    Changelog:
        5/10 Dylan: Initial implementation
    '''
    salt = os.urandom(32)
    user.salt = salt
    user.password_hash = hashlib.pbkdf2_hmac('sha256', pswd.encode('utf-8'), salt, 10000)


def checkPswd(user, pswd):
    '''


    Changelog:
        5/10 Dylan: Initial implementation
    '''
    salt = user.salt
    new_pswd = hashlib.pbkdf2_hmac('sha256', pswd.encode('utf-8'), salt, 10000)
    
    return user.password_hash == new_pswd

def generateAvailability(user, date):
    '''


    Changelog:
        5/10 Dylan: Initial implementation
    '''

    dt = datetime.datetime.combine(date, user.start_time)
    times=[]
    while dt.time() < user.end_time:
        event = Event.query.filter_by(user_id=user.id, datetime=dt).first()
        if event is None:
            times.append((dt.time(), dt.strftime('%I:%M %p')))
        dt = dt + datetime.timedelta(minutes=user.meeting_length)
    
    return times


