from flask import render_template, redirect, url_for, flash, current_app, Blueprint
from .forms import SignUpForm, LoginForm  # Import your form
from .tables import User
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])
def login(message=None):
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        session = current_app.config['SESSION']

        user = session.query(User).filter_by(email=email).first()

        if user:
            if user.verify_password(password, user.password):
                login_user(user)
                return redirect('admin.admin')
            else:
                flash('Incorrect Email or Password')
        else:
            flash('Account does not exist please Sign Up')
    return render_template('login.html', mess=message, form=form)


@auth.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        password1 = form.password.data
        password2 = form.confirm_password.data

        if password1 == password2:
            session = current_app.config['SESSION']
            new_user = User()
            new_user.name=name,
            new_user.email=email,
            new_user.telephone=phone,
            new_user.password=new_user.hash_password(password1)
            try:
                session.add(new_user)
                session.commit()
                flash('Account created successfully!', 'success')
                message = 'Account created successfully! Please Login!'
                return redirect(url_for('auth.login',message=message )) 
            except Exception as e:
                print(e)
                flash("Can't create the Account, Email already exist")

            form.email.data = ''
            form.username.data = ''
            form.password1.data = ''
            form.password2.data = ''
    return render_template('signup.html', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user()
    return redirect('/')


@auth.route('/profile/<int:customer_id>')
@login_required
def profile(user_id):
    session = current_app.config['SESSION']
    user = session.query(User).ger(user_id)
    return render_template('profile.html', user=user_id)