import os
from dotenv import load_dotenv

load_dotenv()  # Carga todo el contenido de .env en variables de entorno

class Config:
    SERVER_NAME = "localhost:5000"
    DEBUG = True

    TEMPLATE_FOLDER = "home/templates/"
    STATIC_FOLDER = "home/static/"
    DATABASE_PATH = "application/api/database/db.sqlite"
    
    API_URL = "http://localhost:5000/api"