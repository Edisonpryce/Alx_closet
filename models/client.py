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
    session = current_app.config['SESSION']
    products = session.query(Product).all()
    carts = session.query(Cart).all()
    items = []
    for product in products:
        items.append(product)
    
    p1 = items[0]
    p2 = items[1]
    p3 = items[2]
    p4 = items[3]
    p5 = items[4]
    p6 = items[5]
    p7 = items[6]
    p8 = items[7]
    p9 = items[8]
    p10 = items[9]
    p11 = items[10]
    p12 = items[11]
    p13 = items[12]
    p14 = items[13]
    p15 = items[14]
    return render_template('/shop.html', p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11, p12=p12, p13=p13, p14=p14, p15=p15, cart=carts)

@customer.route('/product_to_buy/<int:product_id>', methods=['GET', 'POST'], strict_slashes=False)
def product_to_buy(product_id):
    session = current_app.config['SESSION']
    carts = session.query(Cart).all()
    product = session.query(Product).filter_by(id=product_id).first()

    return render_template('/product_to_buy.html', product=product, cart=carts) 


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


@customer.route('/pluscart/<int:cart_id>')
@login_required
def plus_cart(cart_id):
    session = current_app.config['SESSION']
    if request.method == 'GET':
        
        cart_product = session.query(Cart).get(cart_id)
        cart_product.quantity = cart_product.quantity + 1
        session.commit()

        cart = session.query(Cart).filter_by(customer_link=current_user.id).all()

        amount = 0

        for product in cart:
            amount += product.product.selected_price * product.quantity

        return redirect(request.referrer)


@customer.route('/minuscart/<int:cart_id>')
@login_required
def minus_cart(cart_id):
    session = current_app.config['SESSION']
    if request.method == 'GET':
    
        cart_product = session.query(Cart).get(cart_id)
        cart_product.quantity = cart_product.quantity - 1
        session.commit()

        cart = session.query().filter_by(customer_link=current_user.id).all()

        amount = 0

        for item in cart:
            amount += item.product.selected_price * item.quantity

        return redirect(request.referrer)


@customer.route('removecart/<int:cart_id>')
@login_required
def remove_cart(cart_id):
    session = current_app.config['SESSION']
    if request.method == 'GET':
        #cart_id = request.args.get('cart_id')
        cart_product = session.query(Cart).get(cart_id)
        session.delete(cart_product)
        session.commit()

        cart = session.query(Cart).filter_by(customer_link=current_user.id).all()
        amount = 0

        for product in cart:
            amount += product.product.selected_price * product.quantity

        return redirect(request.referrer)