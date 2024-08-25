from flask import Blueprint

admin = Blueprint('admin', __name__)

@admin.route('/admin')
def admins():
    return "This is the admin page"

