from flask import g
from flask.ext.restful import reqparse
from flask.ext.restful import Resource
from flask.ext.restful import marshal_with
from flask.ext.restful import fields
from models.user import User
from db import session
from resources import auth


fields = {
    'id': fields.Integer,
    'username': fields.String,
}


class UsersResource(Resource):
    @marshal_with(fields)
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


class UserResource(Resource):
    @auth.login_required
    @marshal_with(fields)
    def get(self):
        return g.user
