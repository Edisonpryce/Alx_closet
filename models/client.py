from flask import Blueprint, render_template


customer = Blueprint('customer', __name__)

customer.route('/customer', methods=['GET', 'POST'], strict_slashes=False)
def customers(customer_id=None):
    return "You have sucessfully logged into the system"