from flask_restplus import Api
from flask import Blueprint
from .main.controller.user_controller import api as customer_routes
from .main.controller.post_controller import api as post_routes

blueprint = Blueprint('api',__name__)
api = Api(blueprint,title='dev_connector',version='1.1',description='dev_connector_api')
api.add_namespace(customer_routes)
api.add_namespace(post_routes)