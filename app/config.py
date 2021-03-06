import os
from dotenv import load_dotenv

load_dotenv()  # Carga todo el contenido de .env en variables de entorno

class Config:
    SERVER_NAME = os.environ.get("SERVER_NAME", "")
    DEBUG = os.environ.get("DEBUG", False)

    TEMPLATE_FOLDER = "home/templates/"
    STATIC_FOLDER = "home/static/"
    DATABASE_PATH = "application/api/database/db.sqlite"
    
    API_URL = os.environ.get("API_URL", "")