from flask import render_template, redirect, url_for, flash, current_app, Blueprint
from .forms import SignUpForm, LoginForm  # Import your form
from .tables import User
import hashlib

auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    session = current_app.config['SESSION']
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = session.query(User).filter_by(email=email).first()

        if user and user.verify_password(password):
            flash('Login successful!', 'success')
            return redirect(url_for('customer.dashboard'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    session = current_app.config['SESSION']
    form = SignUpForm()
    if form.validate_on_submit():
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
        return redirect(url_for('auth.signup')) 

    return render_template('login.html', form=form)