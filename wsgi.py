# wsgi.py
# pylint: disable=missing-docstring
# import os
# import logging
# logging.warn(os.environ["DUMMY"])
BASE_URL = '/api/v1'
from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow  # NEW LINE (L'ordre est important ici !)
db = SQLAlchemy(app)
ma = Marshmallow(app)  # NEW LINE
from models import Product
from schemas import many_product_schema
from flask_migrate import Migrate
migrate = Migrate(app, db)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World! SQL", 200
@app.route(f'{BASE_URL}/products', methods=['GET'])
def get_many_product():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return many_product_schema.jsonify(products), 200