#!/usr/bin/python3 
""" Main entry of the flask application
"""
from flask import Flask
from models.admin import admin
from models.pages import page 
from models.auth import auth
from models.client import customer
from models.db_storage import DBStorage
from flask_login import  LoginManager
from models.auth import User
from flask import render_template
import secrets


app = Flask(__name__)
token = secrets.token_urlsafe(16)
app.secret_key = token

db = DBStorage()
db.reload()
app.config['SESSION'] = db._DBStorage__session

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'auth.login'
@login_manager.user_loader

def load_user(id):
    return db._DBStorage__session.query(User).get(id) 

app.register_blueprint(page, url_prefix='/')
app.register_blueprint(admin, url_prefix='/') 
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(customer, url_prefix='/')

app.teardown_appcontext
def remove_session(exception):
    db._DBStorage__session.remove()


# Error handling route
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
