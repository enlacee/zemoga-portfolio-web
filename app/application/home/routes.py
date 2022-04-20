from flask import render_template, Blueprint
import requests

from config import Config
# from . import home

API_URL = Config.API_URL
home_scope = Blueprint("home_scope", __name__)

@home_scope.route('/')
@home_scope.route('/home')
def index():
    data = {}
    URL = API_URL + "/users/4"
    try:
        r = requests.get(url = URL)
        data = r.json() # extracting data in json format
    except requests.exceptions.RequestException as error:
        pass

    return render_template('index.html', data=data)