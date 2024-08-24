from flask import Flask, render_template, request

app = Flask(__name__)

app.route('/')
def hello():
    name = request.args["name"]
    render_template("index.html", name=name)