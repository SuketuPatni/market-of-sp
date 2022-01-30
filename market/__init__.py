from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # to ignore FSADeprecationWarning
app.config['SECRET_KEY'] = "cb93e5e80e1c20aaf7cad99c"

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from market import routes