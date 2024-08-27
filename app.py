#!/usr/bin/python3 
from flask import Flask
from models.admin import admin
from models.auth import auth
from models.pages import page as pg
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


app = Flask(__name__)
app.config['SECRETE_KEY'] = 'uekhkaekjnkjankjenkjnekakejkjaekjakje@@1333'


app.register_blueprint(pg, url_prefix='/')
app.register_blueprint(admin, url_prefix='/') # localhost:5000/admin
app.register_blueprint(auth, url_prefix='/auth')  # localhost:5000/auth/login

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)