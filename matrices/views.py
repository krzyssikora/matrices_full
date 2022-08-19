from matrices import app
from flask import render_template, request


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/help')
def help():
    return render_template('help.html')
