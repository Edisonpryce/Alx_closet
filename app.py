#!/usr/bin/python3 
from flask import Flask
from models.admin import admin
from models.pages import page 
from models.auth import auth
from models.client import customer
from models.db_storage import DBStorage
import secrets


app = Flask(__name__)
foo = secrets.token_urlsafe(16)
app.secret_key = foo

db = DBStorage()
db.reload()
app.config['SESSION'] = db._DBStorage__session


app.register_blueprint(page, url_prefix='/')
app.register_blueprint(admin, url_prefix='/') 
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(customer, url_prefix='/')

app.teardown_appcontext
def remove_session(exception):
    db._DBStorage__session.remove()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
