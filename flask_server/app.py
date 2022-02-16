from flask import Flask, send_from_directory
from flask.blueprints import Blueprint
from flask_server.routes import COUPON_BLUEPRINT
import config
from flask_cors import CORS,cross_origin

app = Flask(__name__,static_folder="react_app/build",static_url_path="")
CORS(app)

app.register_blueprint(COUPON_BLUEPRINT)

@app.route('/')
@cross_origin
def serve():
    return send_from_directory(app.static_folder,"index.html")

app.run()