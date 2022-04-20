from flask import Flask
from config import Config

# Integration way 01
from .home import home

# Integration way 02
from .api.routers.api import api_scope
from .api.routers.errors import errors_scope 

# app = Flask(__name__)
app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)

# Here register routers
app.register_blueprint(home)
app.register_blueprint(api_scope, url_prefix="/api")
app.register_blueprint(errors_scope)
