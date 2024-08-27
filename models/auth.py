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
    if form.validate_on_submit():
        # Process the form data
        username = form.username.data
        email = form.email.data
        phone = form.phone.data
        password = form.password.data
        
        # Here you would typically save the user to your database
        # For example:
        # new_user = User(username=username, email=email, phone=phone)
        # new_user.set_password(password)
        # db.session.add(new_user)
        # db.session.commit()
        
        flash('Account created successfully!', 'success')
        return redirect(url_for('login')) 
    return render_template("sign_up.html", form=form)

