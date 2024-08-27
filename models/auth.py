from flask import Blueprint, render_template
from forms import LoginForm, SignUpForm, PasswordChangeForm
from models.db_storage import DBStorage as db



auth = Blueprint('auth', __name__)

@auth.route('/', strict_slashes=False)
@auth.route('/login', strict_slashes=False)
def authentication():
    return render_template("login.html")


@auth.route('/sign-up', method=['GET', 'POST'], strict_slashes=False)
def sign_up():
    form = SignUpForm()
    return render_template("sign_up.html", form=form)

