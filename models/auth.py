from flask import render_template, redirect, url_for, flash, current_app, Blueprint
from models.auth import auth  # Assuming Blueprint is set up
from .forms import SignUpForm  # Import your form
from .tables import User
import hashlib

autho = Blueprint('autho', __name__)


@auth.route('/', strict_slashes=False)
@auth.route('/login', strict_slashes=False)
def authentication():
    return render_template("login.html")

@auth.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # Assuming you have a method to save data from the form to the database
        session = current_app.config['SESSION'] 
        username = form.username.data
        email = form.email.data
        phone = form.phone.data
        password = form.password.data

        session.add(User(
            username=username,
            email=email,
            telephone=phone,
            password=hashlib.md5(password.encode()).hexdigest()
        ))
        session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('admin.admins')) 

    return render_template('login.html', form=form)