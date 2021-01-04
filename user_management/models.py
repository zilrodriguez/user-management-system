from sqlalchemy.sql import func
from flask_login import UserMixin
from user_management import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
# Database models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    user_role = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    def __init__(self, email, password, user_role):
        self.email = email
        self.password = password
        self.user_role = user_role