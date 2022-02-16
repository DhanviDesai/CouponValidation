from flask import Flask, send_from_directory
from flask.blueprints import Blueprint
import flask_server.routes as routes
import flask_server.config as config
from flask_cors import CORS,cross_origin

server = Flask(__name__,static_folder="react_app/build")
CORS(server)

for blueprint in vars(routes).values():
    if isinstance(blueprint,Blueprint):
        server.register_blueprint(blueprint)

@server.route('/')
def serve():
    return send_from_directory(server.static_folder,"index.html")

server.run(port=config.PORT)