from flask import Blueprint, render_template


page = Blueprint('pages', __name__)

@page.route('/add_to_cart/<item_id>', strict_slashes=False)
def home():
    return render_template("index.html")