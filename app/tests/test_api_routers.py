from http import client
from flask import Flask

from application.api.routers.api import api_scope
from config import Config

# Testing the api service (API REST used)
def test_main_service():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(api_scope, url_prefix="/api")
    client = app.test_client()
    url = '/api/users/4'
    response = client.get(url)
    assert response.content_type == "application/json"
    assert response.status_code == 200