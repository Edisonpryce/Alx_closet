from flask import Blueprint, render_template, redirect, flash, url_for
from models.forms import LoginForm, SignUpForm, PasswordChangeForm
from models.db_storage import DBStorage
from models.tables import User

db = DBStorage()
customer = User(username='Edisonasare', email="edison@gmail.com", password='1221oos',telephone='0553650094')
auth = Blueprint('auth', __name__)

@auth.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    db.close()

@auth.route('/', strict_slashes=False)
@auth.route('/login', strict_slashes=False)
def authentication():
    return render_template("login.html")


@auth.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup(): 
    
    return render_template("signup.html")
