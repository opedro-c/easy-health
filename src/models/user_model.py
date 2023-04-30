from flask_login import UserMixin
from models import db


class UserModel(UserMixin, db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    active = db.Column(db.Boolean, nullable=False, default=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String, nullable=False)
