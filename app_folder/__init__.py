from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

myFlaskObj = Flask(__name__)
myFlaskObj.config.from_object(Config)

db = SQLAlchemy(app) 

from app_folder import routes, models

