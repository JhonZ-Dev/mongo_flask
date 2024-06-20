from flask import Flask
from app.config import Config
from pymongo import MongoClient
from app.routes.productos_routes import productos_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Conexión a MongoDB
    client = MongoClient(app.config['MONGO_URI'])
    app.db = client[app.config['MONGO_DB_NAME']]

    # Registro de Blueprints
    app.register_blueprint(productos_bp, url_prefix='/productos')

    return app
