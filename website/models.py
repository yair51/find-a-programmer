from flask_login.mixins import UserMixin
from sqlalchemy.orm import backref
from . import db
# from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    profile = db.relationship('Profile', backref=db.backref('user'))

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    graduation_year = db.Column(db.Integer)
    interests = db.Column(db.String(150))
    skills = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
