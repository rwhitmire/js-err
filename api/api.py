from flask import Flask
from flask.ext.restful import Api
from flask.ext.cors import CORS
from resources.errors import ErrorsResource
from resources.users import UserResource
from resources.users import UsersResource
from resources.token import TokenResource
from resources.site_users import SiteUsersResource

app = Flask(__name__)
api = Api(app)
cors = CORS(app)


api.add_resource(TokenResource, '/token', endpoint='token')
api.add_resource(ErrorsResource, '/errors', endpoint='errors')
api.add_resource(UsersResource, '/users', endpoint='users')
api.add_resource(UserResource, '/user', endpoint='user')
api.add_resource(SiteUsersResource, '/site_users', endpoint='site_users')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
