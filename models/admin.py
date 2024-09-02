""" Page dedicated for adminstration activities of the web application
"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .tables import User, Product, Order
from .forms import  ShopItemsForm

admin = Blueprint('admin', __name__)

@admin.route('/dashboard', strict_slashes=False)
@login_required
def dashboard():
    return render_template('admin.html', user=current_user.name)


@admin.route('/add-shop-items', methods=['GET', 'POST'])
@login_required
def add_shop_items():
    if current_user.id:
        form = ShopItemsForm()

        if form.validate_on_submit():
            product_name = form.product_name.data
            minimum_price = form.min_price.data
            maximum_price = form.max_price.data
            in_stock = form.in_stock.data

            file = form.product_picture.data

            file_name = secure_filename(file.filename)

            file_path = f'../product_media/{file_name}'

            file.save(file_path)

            item_to_add = Product()
            item_to_add.product_name = product_name
            item_to_add.minimum_price = min_price
            item_to_add.maximum_price = max_price
            item_to_add.in_stock = in_stock
        
            item_to_add.product_picture = file_path

            try:
                db.session.add(new_shop_item)
                db.session.commit()
                flash(f'{product_name} added Successfully')
                print('Product Added')
                return render_template('add_shop_items.html', form=form)
            except Exception as e:
                print(e)
                flash('Product Not Added!!')

        return render_template('add_shop_items.html', form=form)

    return render_template('404.html')

