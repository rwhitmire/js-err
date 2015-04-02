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
}


class ErrorResource(Resource):
    decorators = [auth.login_required]

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
        args = parser.parse_args()

        error = Error(
            date=args['date'],
            message=args['message'],
            url=args['url'],
            line=args['line'],
            column=args['column'],
            stack=args['stack'],
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
