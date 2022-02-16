from flask import Flask, send_from_directory
from flask.blueprints import Blueprint
import flask_server.routes as routes
import flask_server.config as config
from flask_cors import CORS,cross_origin

app = Flask(__name__,static_folder="react_app/build")
CORS(app)

for blueprint in vars(routes).values():
    if isinstance(blueprint,Blueprint):
        app.register_blueprint(blueprint)

@app.route('/')
@cross_origin
def serve():
    return send_from_directory(app.static_folder,"index.html")

# server.run(port=config.PORT)