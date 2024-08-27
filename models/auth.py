from flask import Blueprint, render_template, redirect, flash, url_for, current_app
from models.forms import LoginForm, SignUpForm, PasswordChangeForm
from models.tables import User


auth = Blueprint('auth', __name__)



@auth.route('/', strict_slashes=False)
@auth.route('/login', strict_slashes=False)
def authentication():
    return render_template("login.html")


@auth.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup(): 
    session = current_app.config['SESSION']
    users = session.query(User).all()

    return render_template("test.html", users=users)
