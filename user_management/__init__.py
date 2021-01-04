from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialize app
app = Flask(__name__)
app.secret_key = '057ce5ed548a606bee78f7045069bc2c'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:admin@localhost/user_management_system"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Create models
db = SQLAlchemy(app)
# Bcrypt
bcrypt = Bcrypt(app)
# Login manager
login_manager = LoginManager(app)

from user_management import routes