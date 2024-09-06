""" Page dedicated for adminstration activities of the web application
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
import os
from werkzeug.utils import secure_filename
from .tables import User, Product, Order
from .forms import  ShopItemsForm, AdminPrivilagesForm

admin = Blueprint('admin', __name__)

@admin.route('/dashboard', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def dashboard():
    session = current_app.config['SESSION']
    users = session.query(User).all()
    admin_form = AdminPrivilagesForm()
    shop_form = ShopItemsForm()

    if request.method == 'POST':
        # Handle Admin Privileges Form
        if 'email' in request.form and admin_form.validate_on_submit():
            email = admin_form.email.data
            user = session.query(User).filter_by(email=email).first()
            if user:
                if user.is_admin:
                    user.is_admin = False
                    message = f"User with email {email} has been demoted from admin."
                else:
                    user.is_admin = True
                    message = f"User with email {email} has been promoted to admin."
                session.commit()
                flash(message, 'success')
            else:
                flash('You do not have permission to change admin privileges.', 'error')
        else:
            flash('User not found.', 'error')
        return redirect(url_for('admin.dashboard'))

        # Handle Add Shop Items Form
    elif 'product_name' in request.form and shop_form.validate_on_submit():
        return add_shop_items(shop_form)

    return render_template('admin.html', user=current_user, admin_form=admin_form, shop_form=shop_form, users=users)


def add_shop_items(form):
    session = current_app.config['SESSION']
    product_name = form.product_name.data
    min_price = form.min_price.data
    max_price = form.max_price.data
    in_stock = form.in_stock.data
    file = form.product_picture.data

    if file:
        # Ensure the upload folder exists
        upload_folder = os.path.join('static', 'product_media')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        file_name = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, file_name)
        file.save(file_path)

    item_to_add = Product(
        product_name=product_name,
        minimum_price=min_price,
        maximum_price=max_price,
        in_stock=in_stock,
        product_picture=file_path
    )

    try:
        session.add(item_to_add)
        session.commit() 
        flash(f'{product_name} added successfully', 'success')
        print('Product Added')
    except Exception as e:
        session.rollback()
        print(f"Error adding product: {e}")
        flash('Product Not Added!!', 'error')

    return redirect(url_for('admin.dashboard'))