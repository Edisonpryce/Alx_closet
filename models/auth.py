from flask import render_template, redirect, url_for, flash, current_app, Blueprint, request
from .forms import SignUpForm, LoginForm, PasswordChangeForm  # Import your form
from .tables import User
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if  request.args.get('message'):
        message = 'Account created successfully!'
    else:
        message = None
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        session = current_app.config['SESSION']

        user = session.query(User).filter_by(email=email).first()

        if user:
            if user.verify_password(password, user.password):
                login_user(user)
                flash('Login Successful', 'success')
                return redirect(url_for('customer.home'))
            else:
                flash('Incorrect Email or Password')
        else:
            flash('Account does not exist please Sign Up')
            message = 'Account does not exist please Sign Up'
    return render_template('login.html', form=form, message=message)


@auth.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        session = current_app.config['SESSION']
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        password1 = form.password.data
        password2 = form.confirm_password.data

        if password1 == password2:
            new_user = User()
            new_user.name=name.capitalize(),
            new_user.email=email,
            new_user.telephone=phone,
            new_user.password=new_user.hash_password(password1)
            try:
                session.add(new_user)
                session.commit()
                flash('Account created successfully!', 'success')
                return redirect(url_for('auth.login', message= 'Account created successfully!')) 
            except Exception as e:
                print(e)
                flash("Can't create the Account, Email already exist")

            form.name.data = ''
            form.email.data = ''
            form.password.data = ''
            #form.password2.data = ''
    return render_template('signup.html', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user()
    return redirect('/')


"""
@auth.route('/profile/<int:customer_id>')
@login_required
def profile(user_id):
    session = current_app.config['SESSION']
    user = session.query(User).ger(user_id)
    return render_template('profile.html', user=user_id)


@auth.route('/change-password/<int:customer_id>', methods=['GET', 'POST'])
@login_required
def change_password(user_id):
    form = PasswordChangeForm()
    session = current_app.config['SESSION']
    user = session.query(User).ger(user_id)
    if form.validate_on_submit():
        current_password = form.current_password.data
        new_password = form.new_password.data
        confirm_new_password = form.confirm_new_password.data

        if user.verify_password(current_password):
            if new_password == confirm_new_password:
                user.password = confirm_new_password
                session.commit()
                flash('Password Updated Successfully')
                return redirect(f'/profile/{user.id}')
            else:
                flash('New Passwords do not match!!')

        else:
            flash('Current Password is Incorrect')

    return render_template('change_password.html', form=form)

"""