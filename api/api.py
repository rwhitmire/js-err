from flask import Flask
from flask.ext.restful import Api
from flask.ext.cors import CORS
from resources.error import ErrorResource
from resources.error import ErrorListResource
from resources.user import UserResource
from resources.user import CurrentUserResource
from resources.token import TokenResource
from resources.site_user import SiteUserResource

app = Flask(__name__)
api = Api(app)
cors = CORS(app)


api.add_resource(TokenResource, '/token')
api.add_resource(ErrorResource, '/errors/<id>')
api.add_resource(ErrorListResource, '/errors')
api.add_resource(UserResource, '/users')
api.add_resource(CurrentUserResource, '/current_user')
api.add_resource(SiteUserResource, '/site_users')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
