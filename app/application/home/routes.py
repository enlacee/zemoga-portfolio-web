from flask import render_template
from . import home

@home.route('/')
@home.route('/home')
def index():
    return render_template('index.html')