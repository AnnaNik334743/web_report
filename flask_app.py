from flask import Flask, jsonify, request
import flask_swagger_ui
import yaml

app = Flask(__name__)


def custom_swagger():
    with open("api_spec.yaml", "r") as file:
        swag = yaml.load(file, Loader=yaml.FullLoader)
    return swag


@app.route('/swagger.json')
def swagger():
    return jsonify(custom_swagger())


# GET endpoint to retrieve a greeting message
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, world!"})


# POST endpoint to create a new greeting message
@app.route("/hello", methods=["POST"])
def create_hello():
    name = request.args.get("name")
    return jsonify({"message": f"Hello, {name}! Greeting message created"})


SWAGGER_URL = '/docs'
API_URL = '/swagger.json'

swaggerui_blueprint = flask_swagger_ui.get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "My API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


if __name__ == "__main__":
    app.run(debug=True)
