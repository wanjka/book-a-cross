from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    email = db.Column(db.String(64), unique=True)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def set_password(self, password_raw):
        self.password = generate_password_hash(password_raw)

    def check_password(self, password_hashed):
        return check_password_hash(self.password, password_hashed)

    def __repr__(self):
        return f'<User, name={self.username}>'
