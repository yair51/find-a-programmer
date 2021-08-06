from flask import Blueprint, render_template
from flask_migrate import current
from . import db
from .models import User, Profile
from flask_login import current_user
#from website import app

views = Blueprint('views', __name__)

@views.route("/")
def home():
    users = db.session.query(User, Profile).outerjoin(Profile, Profile.user_id == User.id)
    for user in users:
        print(user)
    return render_template("index.html", title="Home", user=current_user, users=users)

@views.route("/profile")
@views.route("/profile/")
def profile():
    return render_template("profile.html", title="Profile", user=current_user)