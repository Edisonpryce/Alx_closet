from flask import render_template, redirect, url_for, flash, current_app, Blueprint
from .forms import SignUpForm, LoginForm  # Import your form
from .tables import User
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user:
            if user.verify_password(password=password):
                login_user(user)
                return redirect('/')
            else:
                flash('Incorrect Email or Password')

        else:
            flash('Account does not exist please Sign Up')

    return render_template('login.html', form=form)


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
                message = "Account created successfully!', kindly login"
                return redirect(url_for('auth.signup')) 
            except Exception as e:
                print(e)
                flash("Can't create the Account, Email already exist")

            form.email.data = ''
            form.username.data = ''
            form.password1.data = ''
            form.password2.data = ''
    return render_template('login.html', form=form)