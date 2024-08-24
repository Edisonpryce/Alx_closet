#!/usr/bin/python3 
from flask import Flask, render_template, request
import os

template_dir = os.path.abspath('../static/templates')
app = Flask(__name__, template_folder=template_dir)


@app.route('/', strict_slashes=False)
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)