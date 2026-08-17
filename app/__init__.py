from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
# object that represents the database
db = SQLAlchemy(app)
# object that represents database migration engine
migrate = Migrate(app, db)
# models module will define the structure of the database
login = LoginManager(app)
from app import routes, models