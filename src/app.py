from flask import Flask
from flask.blueprints import Blueprint
import routes
import config

server = Flask(__name__)

for blueprint in vars(routes).values():
    if isinstance(blueprint,Blueprint):
        server.register_blueprint(blueprint)

server.run(port=config.PORT)