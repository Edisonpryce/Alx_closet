""" This is the customer only accessible page.
contains the home page and the index page
which is the main page of the website.
This is the main page of the website.
"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user


customer = Blueprint('customer', __name__)

@customer.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    return render_template('/index.html')

@customer.route('/shop.html', methods=['GET', 'POST'], strict_slashes=False)
def shop():
    return render_template('/shop.html')

@customer.route('/product1', methods=['GET', 'POST'], strict_slashes=False)
def product1():
    return render_template('/product1.html')

@customer.route('/product2', methods=['GET', 'POST'], strict_slashes=False)
def product2():
    return render_template('/product2.html')

@customer.route('/product3', methods=['GET', 'POST'], strict_slashes=False)
def product3():
    return render_template('/product3.html')

@customer.route('/product4', methods=['GET', 'POST'], strict_slashes=False)
def product4():
    return render_template('/product4.html')

@customer.route('/product5', methods=['GET', 'POST'], strict_slashes=False)
def product5():
    return render_template('/product5.html')

@customer.route('/product6', methods=['GET', 'POST'], strict_slashes=False)
def product6():
    return render_template('/product6.html')

@customer.route('/product7', methods=['GET', 'POST'], strict_slashes=False)
def product7():
    return render_template('/product7.html')

@customer.route('/product8', methods=['GET', 'POST'], strict_slashes=False)
def product8():
    return render_template('/product8.html')

@customer.route('/product9', methods=['GET', 'POST'], strict_slashes=False)
def product9():
    return render_template('/product9.html')

@customer.route('/product10', methods=['GET', 'POST'], strict_slashes=False)
def product10():
    return render_template('/product10.html')

@customer.route('/product11', methods=['GET', 'POST'], strict_slashes=False)
def product11():
    return render_template('/product11.html')

@customer.route('/product12', methods=['GET', 'POST'], strict_slashes=False)
def product12():
    return render_template('/product12.html')

@customer.route('/product13', methods=['GET', 'POST'], strict_slashes=False)
def product13():
    return render_template('/product13.html')



@customer.route('/home', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def home():
    return render_template('/home.html', user=current_user)

@customer.route('/cart', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def cart():
    return "Welcome to your cart page"

@customer.route('/favorite_products', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def favorite_products():
    return "Welcome to  your favorite products page"


@customer.route('/profile', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def profile():
    
    return render_template('/profile.html', user=current_user)


