""" Page dedicated for adminstration activities of the web application
"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user

admin = Blueprint('admin', __name__)

@admin.route('/dashboard', strict_slashes=False)
@login_required
def dashboard():
    return render_template('admin.html', user=current_user.name)

