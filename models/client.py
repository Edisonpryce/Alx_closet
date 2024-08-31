from flask import Blueprint, render_template
from flask_login import login_required, current_user


customer = Blueprint('customer', __name__)

@customer.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    return render_template('/index.html')

@customer.route('/home', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def home():
    return render_template('/home.html', user=current_user.name)
