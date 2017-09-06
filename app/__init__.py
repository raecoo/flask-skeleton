# Import flask and template operators
import os

from flask import Flask, render_template, Blueprint
from lib.flask_extended import Flask
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
import flask_restful as restful

from api.v1.hello_world import HelloWorld

blueprint_api_v1 = Blueprint('api_v1', __name__)
# Define the WSGI application object
app = Flask(__name__)
# Configurations
app.config.from_yaml(os.path.join(app.root_path, '../config.yml'))

api = restful.Api(blueprint_api_v1, prefix="/v1")
api.add_resource(HelloWorld, '/helloworld')

# Define the database object which is imported by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.auth.controllers import auth as auth_module

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(blueprint_api_v1)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
