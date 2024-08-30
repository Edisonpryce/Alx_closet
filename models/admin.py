from flask import Blueprint
from flask_login import login_required, current_user

admin = Blueprint('admin', __name__)

@admin.route('/admin', strict_slashes=False)
@login_required
def admins():
    return "This is the admin page"

