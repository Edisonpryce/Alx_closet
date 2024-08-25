#!/usr/bin/python3 
from flask import Flask

app = Flask(__name__)
app.config['SECRETE_KEY'] = 'uekhkaekjnkjankjenkjnekakejkjaekjakje@@1333'
from models.admin import admin
from models.auth import auth
from models.pages import pages


app.register_blueprint(pages, url_prefix='/')
app.register_blueprint(admin, url_prefix='/') # localhost:5000/admin
app.register_blueprint(auth, url_prefix='/auth')  # localhost:5000/auth/login

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)