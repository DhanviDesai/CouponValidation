from flask import Flask
from flask.blueprints import Blueprint
import flask_server.routes as routes
import flask_server.config as config

server = Flask(__name__)

for blueprint in vars(routes).values():
    if isinstance(blueprint,Blueprint):
        server.register_blueprint(blueprint)

server.run(port=config.PORT)