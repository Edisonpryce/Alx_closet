""" Page dedicated for adminstration activities of the web application
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app, send_from_directory
from flask_login import login_required, current_user, logout_user
import os
from werkzeug.utils import secure_filename
from .tables import User, Product, Order
from .forms import  ShopItemsForm, AdminPrivilagesForm


admin = Blueprint('admin', __name__)

# Admin dashboard route
@admin.route('/dashboard', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def dashboard():
    session = current_app.config['SESSION']
    users = session.query(User).all()
    admin_form = AdminPrivilagesForm()

    if admin_form.validate_on_submit():
        print("Shop form validation passed")
        email = admin_form.email.data
        user = session.query(User).filter_by(email=email).first()
        if user:
            if current_user.is_admin:
                user.is_admin = not user.is_admin
                message = f"User with email {email} has been {'promoted to' if user.is_admin else 'demoted from'} admin."
                session.commit()
                flash(message, 'success')
            else:
                flash('You do not have permission to change admin privileges.', 'error')
                return redirect(url_for('auth.logout'))
        else:
            flash('User not found.', 'error')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin.html', user=current_user, admin_form=admin_form, users=users)


@admin.route('/media/<path:filename>')
def get_image(filename):
    return send_from_directory('../media', filename)

@admin.route('/add_to_shop', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def add_to_shop():
    session = current_app.config['SESSION']
    users = session.query(User).all()
    shop_form = ShopItemsForm()

    if shop_form.validate_on_submit():

        product_name = shop_form.product_name.data
        gender = shop_form.gender.data
        min_price = shop_form.min_price.data
        max_price = shop_form.max_price.data
        selected_price = shop_form.selected_price.data
        in_stock = shop_form.in_stock.data
        description = shop_form.description.data

        file = shop_form.product_picture.data

        file_path = None
        if file:
            upload_folder = os.path.join('static', 'product_media')
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            file_name = secure_filename(file.filename)
            file_path = file_name
            file.save(os.path.join(upload_folder, file_name))

        item_to_add = Product(
            product_name=product_name,
            gender=gender,
            min_price=min_price,
            max_price=max_price,
            selected_price=selected_price,
            in_stock=in_stock,
            description=description,
            product_picture=file_path if file_path else ''
        )

        try:
            session.add(item_to_add)
            session.commit()
            flash(f'{product_name} added successfully', 'success')
        except Exception as e:
            session.rollback()
            flash('Product Not Added!!', 'error')
            print(f"Error adding product: {e}")

        return redirect(request.referrer)

    return render_template('add_to_shop.html', user=current_user, shop_form=shop_form, users=users)

@admin.route('/products')
@login_required
def products():
    if current_user.is_admin:
        session = current_app.config['SESSION']
        products = session.query(Product).order_by(Product.id).all()
        return render_template('products.html', user=current_user, products=products)
    else:
        return redirect(url_for('auth.login'))
   
@admin.route('/update-product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def update_product(product_id):
    if current_user.is_admin:
        form = ShopItemsForm()
        session = current_app.config['SESSION']
        product_to_update = session.query(Product).get(product_id)

        form.product_name.render_kw = {'placeholder': product_to_update.product_name}
        form.gender.render_kw = {'placeholder': product_to_update.gender}
        form.min_price.render_kw = {'placeholder': product_to_update.min_price}
        form.max_price.render_kw = {'placeholder': product_to_update.max_price}
        form.in_stock.render_kw = {'placeholder': product_to_update.in_stock}
        form.selected_price.render_kw = {'placeholder': product_to_update.selected_price}

        if form.validate_on_submit():
            product_name = form.product_name.data
            gender = form.gender.data
            min_price = form.min_price.data
            max_price = form.max_price.data
            in_stock = form.in_stock.data
            selected_price = form.selected_price.data

            file = form.product_picture.data

            file_path = None
            if file:
                upload_folder = os.path.join('static', 'product_media')
                file_name = secure_filename(file.filename)
                file_path = os.path.join(upload_folder, file_name)
                file.save(file_path)

            try:
                session.query(Product).filter_by(id=product_id).update(dict(product_name=product_name,
                                                                gender=gender,
                                                                min_price=min_price,
                                                                max_price=max_price,
                                                                in_stock=in_stock,
                                                                selected_price=selected_price,
                                                                product_picture=file_path))

                session.commit()
                flash(f'{product_name} updated Successfully')
                print('Product Upadted')
                return redirect(url_for('admin.products'))
            except Exception as e:
                print("Product wasn't Updated", e)
                flash("Product wasn't Updated!!!")

        return render_template('update_product.html', shop_form=form)
    return render_template('404.html')


@admin.route('/delete-product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def delete_product(product_id):
    if current_user.is_admin:
        session = current_app.config['SESSION']

        try:
            product_to_delete = session.query(Product).get(product_id)
            session.delete(product_to_delete)
            session.commit()
            flash('Product deleted successfully')
            return redirect(url_for('admin.products'))
        except Exception as e:
            print("Product wasn't deleted", e)
            flash("Product wasn't deleted!!")
        return redirect(url_for('admin.products'))

    return render_template('404.html')
