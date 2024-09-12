""" This is the customer only accessible page.
contains the home page and the index page
which is the main page of the website.
This is the main page of the website.
"""

from flask import Blueprint, render_template, redirect, url_for, request, current_app, flash, jsonify
from flask_login import login_required, current_user, logout_user
from .tables import Product, Cart

customer = Blueprint('customer', __name__)


@customer.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        session = current_app.config['SESSION']
        search_query = request.form.get('search')
        products = session.query(Product).filter(Product.product_name.ilike(f'%{search_query}%')).all()
        return render_template('search.html', products=products, cart=session.query(Cart).filter_by(customer_link=current_user.id).all()
                           if current_user.is_authenticated else [])

    return render_template('search.html')

@customer.route('/shop.html', methods=['GET', 'POST'], strict_slashes=False)
def shop():
    return render_template('/shop.html')

@customer.route('/product_to_buy/<int:product_id>', methods=['GET', 'POST'], strict_slashes=False)
def product_to_buy(product_id):
    session = current_app.config['SESSION']
    product = session.query(Product).filter_by(id=product_id).first()

    return render_template('/product_to_buy.html', product=product) 


@customer.route('/favorite_products', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def favorite_products():
    return "Welcome to  your favorite products page"


@customer.route('/add-to-cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    session = current_app.config['SESSION']
    product = session.query(Product).filter_by(id=product_id).first()
    selected_product = session.query(Cart).filter_by(product_link=product_id, customer_link=current_user.id).first()
    if selected_product:
        try:
            selected_product.quantity = selected_product.quantity + 1
            session.commit()
            flash(f' Quantity of { selected_product.product.product_name } has been updated')
            return redirect(request.referrer)
        except Exception as e:
            print('Quantity not Updated', e)
            flash(f'Quantity of { selected_product.product.product_name } not updated')
            return redirect(request.referrer)

    new_cart_product = Cart()
    new_cart_product.quantity = 1
    new_cart_product.product_link = product.id
    new_cart_product.customer_link = current_user.id

    try:
        session.add(new_cart_product)
        session.commit()
        flash(f'{new_cart_product.product.product_name} added to cart')
    except Exception as e:
        print('Item not added to cart', e)
        flash(f'{new_cart_product.product.product_name} has not been added to cart')

    return redirect(request.referrer)


@customer.route('/cart')
@login_required
def display_cart_items():
    session = current_app.config['SESSION']
    cart = session.query(Cart).filter_by(customer_link=current_user.id).all()
    amount = 0
    for product in cart:
        amount += product.product.selected_price * product.quantity

    return render_template('cart.html', cart=cart, amount=amount, total=amount+0)


@customer.route('/pluscart')
@login_required
def plus_cart():
    session = current_app.config['SESSION']
    if request.method == 'GET':
        cart_id = request.args.get('cart_id')
        cart_product = session.query(Cart).get(cart_id)
        cart_product.quantity = cart_product.quantity + 1
        session.commit()

        cart = session.query(Cart).filter_by(customer_link=current_user.id).all()

        amount = 0

        for product in cart:
            amount += product.product.current_price * product.quantity

        data = {
            'quantity': cart_product.quantity,
            'amount': amount,
            'total': amount + 0
        }

        return jsonify(data)


@customer.route('/minuscart')
@login_required
def minus_cart():
    session = current_app.config['SESSION']
    if request.method == 'GET':
        cart_id = request.args.get('cart_id')
        cart_product = session.query(Cart).get(cart_id)
        cart_product.quantity = cart_product.quantity - 1
        session.commit()

        cart = session.query().filter_by(customer_link=current_user.id).all()

        amount = 0

        for item in cart:
            amount += item.product.current_price * item.quantity

        data = {
            'quantity': cart_product.quantity,
            'amount': amount,
            'total': amount + 0
        }

        return jsonify(data)


@customer.route('removecart')
@login_required
def remove_cart():
    session = current_app.config['SESSION']
    if request.method == 'GET':
        cart_id = request.args.get('cart_id')
        cart_product = session.query(Cart).get(cart_id)
        session.delete(cart_product)
        session.commit()

        cart = session.query(Cart).filter_by(customer_link=current_user.id).all()

        amount = 0

        for product in cart:
            amount += product.product.current_price * product.quantity

        data = {
            'quantity': cart_product.quantity,
            'amount': amount,
            'total': amount + 0
        }

        return jsonify(data)