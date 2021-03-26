from app.main.config import config_by_name
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from .model.customer_model import Customer

app = Flask(__name__,static_url_path='/static')
db = SQLAlchemy()
ma = Marshmallow(app)


def create_app(config_name):
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    with app.app_context():
        db.create_all()
    return app
