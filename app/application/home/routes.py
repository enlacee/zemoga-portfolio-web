from flask import render_template
import requests

from config import Config
from . import home

API_URL = Config.API_URL

@home.route('/')
@home.route('/home')
def index():
    data = {}
    URL = API_URL + "/users/4"
    try:
        r = requests.get(url = URL)
        data = r.json() # extracting data in json format
    except requests.exceptions.RequestException as error:
        pass

    return render_template('index.html', data=data)