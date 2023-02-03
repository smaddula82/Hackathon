from flask import Flask, jsonify
from apispec import APISpec
from flask_restful import Resource, Api
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

application = Flask(__name__)
application.secret_key = 'house-saleprice-1234'

api = Api(application)  # Flask restful wraps Flask app around it.

application.config.update({
    'APISPEC_SPEC': APISpec(
        title='House Saleprice Prediction Model',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(application)

@application.route("/")
def show():
    return '<h1>Welcome to House Saleprice Prediction Model</h1><br>Please <a href="http://127.0.0.1:8000/swagger-ui">Click</a> here to go list of API'

#application.run()