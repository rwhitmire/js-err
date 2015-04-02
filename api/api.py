from flask import Flask
from flask.ext.restful import Api
from resources import ErrorResource
from resources import UserResource
from resources import TokenResource

app = Flask(__name__)
api = Api(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


api.add_resource(TokenResource, '/token', endpoint='token')
api.add_resource(ErrorResource, '/errors', endpoint='errors')
api.add_resource(UserResource, '/users', endpoint='users')

if __name__ == '__main__':
    app.run(debug=True)
