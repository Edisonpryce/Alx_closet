from flask import Blueprint
from . import storage

auth = Blueprint('auth', __name__)

@auth.route('/login')
def authdentication():
    return "This is the login page"

@auth.route('/sign-up')
def sign_up():
    return "This is the sign up page"

