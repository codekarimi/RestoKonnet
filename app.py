#!/usr/bin/python3
from models import storage
from flask import Flask, jsonify
from api.v1.views import app_views
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from api.v1.auth import BLACK_LIST_TOKEN
from api.v1.vendor_auth import mail
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mail.init_app(app)

app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
jwt = JWTManager(app)

SWAGGER_URL = "/api/v1/swagger"
API_URL = "http://petstore.swagger.io/v2/swagger.json"

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "RestoKonnect API"},  # Swagger UI config overrides
)
app.register_blueprint(swaggerui_blueprint)


@jwt.token_in_blocklist_loader
def check_if_token_blacklist(jwt_header, jwt_data):
    jti = jwt_data["jti"]
    return jti in BLACK_LIST_TOKEN


@app.route("/", methods=["GET"], strict_slashes=False)
def home():
    """home route"""
    return jsonify({"Home": "Welcome to RestoKonnect API"})


@app.teardown_appcontext
def close_db(error):
    """Close Storage"""
    storage.close()


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port=5001, threaded=True)
