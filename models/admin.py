from flask import Blueprint

admin = Blueprint('admin', __name__)

@admin.route('/admin', strict_slashes=False)
def admins():
    return "This is the admin page"

