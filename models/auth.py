from flask import Blueprint, render_template
from models.db_storage import DBStorage



auth = Blueprint('auth', __name__)

@auth.route('/', strict_slashes=False)
@auth.route('/login', strict_slashes=False)
def authentication():
    return render_template("login.html")

@auth.route('/sign-up', strict_slashes=False)
def sign_up():
    return render_template("sign_up.html")

