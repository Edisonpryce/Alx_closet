from flask import Blueprint, render_template
from models.db_storage import DBStorage



auth = Blueprint('auth', __name__)

@auth.route('/login')
def authdentication():
    return render_template("login.html")

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

