from flask.ext.restful import Resource
from flask.ext.restful import reqparse
from db import session
from models.user import User


class TokenResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('password')
        args = parser.parse_args()

        user = session.query(User).filter_by(username = args['username']).first()

        if user is None:
            return {}, 400

        if user.verify_password(args['password']):
            token = user.generate_auth_token()
            return {'token': token}, 200

        return {}, 400
