from flask import Blueprint, render_template


page = Blueprint('pages', __name__)

@page.route('/', strict_slashes=False)
def home_page():
    return render_template("index.html")