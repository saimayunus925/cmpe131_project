import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    
    """ Prevent attack in application. 
    
    4/19 Ali
    
    """
    
    SECRET_KEY = 'shh.. This-is-a-secret'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
