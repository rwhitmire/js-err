from models import Error
from models import User
from db import session

from flask import g
from flask.ext.restful import reqparse
from flask.ext.restful import Resource
from flask.ext.restful import fields
from flask.ext.restful import marshal_with
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = session.query(User).filter_by(username = username_or_token).first()

        if not user or not user.verify_password(password):
            return False

    g.user = user
    return True


error_fields = {
    'id': fields.Integer,
    'date': fields.DateTime,
    'message': fields.String,
    'url': fields.String,
    'line': fields.Integer,
    'column': fields.Integer,
    'stack': fields.String,
    'app_code_name': fields.String,
    'app_name': fields.String,
    'app_version': fields.String,
    'cookie_enabled': fields.String,
    'language': fields.String,
    'platform': fields.String,
    'product': fields.String,
    'user_agent': fields.String,
    'vendor': fields.String,
}


class ErrorResource(Resource):
    @auth.login_required
    @marshal_with(error_fields)
    def get(self):
        return session.query(Error).all()

    @marshal_with(error_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('date')
        parser.add_argument('message')
        parser.add_argument('url')
        parser.add_argument('line')
        parser.add_argument('column')
        parser.add_argument('stack')
        parser.add_argument('app_code_name')
        parser.add_argument('app_name')
        parser.add_argument('app_version')
        parser.add_argument('cookie_enabled')
        parser.add_argument('language')
        parser.add_argument('platform')
        parser.add_argument('product')
        parser.add_argument('user_agent')
        parser.add_argument('vendor')
        args = parser.parse_args()

        error = Error(
            date=args['date'],
            message=args['message'],
            url=args['url'],
            line=args['line'],
            column=args['column'],
            stack=args['stack'],
            app_code_name=args['app_code_name'],
            app_name=args['app_name'],
            app_version=args['app_version'],
            cookie_enabled=args['cookie_enabled'],
            language=args['language'],
            platform=args['platform'],
            product=args['product'],
            user_agent=args['user_agent'],
            vendor=args['vendor'],
        )

        session.add(error)
        session.commit()

        return error, 201


user_fields = {
    'id': fields.Integer,
    'username': fields.String,
}


class UserResource(Resource):
    @marshal_with(user_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('password')
        args = parser.parse_args()

        user = User(username=args['username'])
        user.hash_password(args['password'])

        session.add(user)
        session.commit()

        return user, 201


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
