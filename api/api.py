from flask import Flask
from flask.ext.restful import Api
from flask.ext.cors import CORS
from resources import ErrorsResource
from resources import UserResource
from resources import UsersResource
from resources import TokenResource

app = Flask(__name__)
api = Api(app)
cors = CORS(app)


api.add_resource(TokenResource, '/token', endpoint='token')
api.add_resource(ErrorsResource, '/errors', endpoint='errors')
api.add_resource(UsersResource, '/users', endpoint='users')
api.add_resource(UserResource, '/user', endpoint='user')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
