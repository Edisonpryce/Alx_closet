""" Auth page dedication for the signing up and loging
and all the logic authentication is handled here
"""
from flask import render_template, redirect, url_for, flash, current_app, Blueprint, request
from .forms import SignUpForm, LoginForm, PasswordChangeForm 
from .tables import User, Product
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/home', methods=['GET', 'POST'], strict_slashes=False)
@auth.route('/', methods=['GET', 'POST'], strict_slashes=False)
def home():
    session = current_app.config['SESSION']
    products = session.query(Product).all()

    if products:
        items = []
        for product in  products:
            items.append(product)
        p1 = items[0]
        p2 = items[1]
        p3 = items[2]
        p4 = items[3]
        p5 = items[4]
        p6 = items[5]
        p7 = items[6]
        p8 = items[7]

        print(f"p1: {p1.product_name} p2: {p2.product_name} p3:{p3.product_name} p4:{p4.product_name} p5:{p5.product_name} p6:{p6.product_name} p7:{p7.product_name} p8:{p8.product_name}")
        return render_template('/home.html', p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8)
    return render_template('home.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        session = current_app.config['SESSION']
        user = session.query(User).filter_by(email=email).first()
        if user.id == 1:
            user.is_admin = True
            session.commit()
        if user:
            if user.verify_password(password, user.password):
                login_user(user)
                if user.is_admin:
                    flash('Welcome Admin!', 'success')
                    return redirect(url_for('admin.dashboard'))
                else:
                    flash('Welcome Customer!', 'success')
                    return redirect(url_for('auth.home'))
            else:
                flash('Incorrect Email or Password')
        else:
            flash('Account does not exist please Sign Up')
    return render_template('login.html', form=form)


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
                return redirect(url_for('auth.login')) 
            except Exception as e:
                print(e)
                flash("Can't create the Account, Email already exist")
        else:
            flash('Passwords do not match')
    return render_template('signup.html', form=form)

@auth.route('/profile/<int:id>', methods=['GET', 'POST'])
@login_required
def profile(id):
    session = current_app.config['SESSION']
    user = session.query(User).get(id)
    
    # Ensure that the current user has permission to view this profile
    if user != current_user:
        flash('You do not have permission to access this profile.', 'error')
        return redirect(url_for('auth.home'))
    
    form = PasswordChangeForm()
    session = current_app.config['SESSION']

    if form.validate_on_submit():
        current_password = form.current_password.data
        new_password = form.new_password.data
        confirm_new_password = form.confirm_new_password.data

        if user.verify_password(current_password, user.password):
            if new_password == confirm_new_password:
                user.password = user.hash_password(confirm_new_password)
                session.commit()
                flash('Password Updated Successfully')
                return redirect(url_for('auth.profile', id=id))  # Redirect with id
            else:
                flash('New Passwords do not match!!')

        else:
            flash('Current Password is Incorrect')

    return render_template('profile.html', form=form, user=user)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user()
    return redirect(url_for('auth.home'))