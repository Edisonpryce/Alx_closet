from flask import Blueprint, render_template


page = Blueprint('pages', __name__)

@page.route('/')
def home_page():
    return render_template("index.html")