from flask.ext.restful import reqparse
from flask.ext.restful import Resource
from flask.ext.restful import marshal_with
from flask.ext.restful import fields
from models.user import User
from models.site_user import SiteUser
from models.site import Site
from db import session

fields = {
    'site.id': fields.Integer,
    'user.id': fields.Integer,
    'site.name': fields.String,
    'user.username': fields.String,
}


def password(password_str):
    if(len(password_str) < 6):
        raise ValueError('password must be at least 6 characters')

    return password_str


class SiteUsersResource(Resource):
    @marshal_with(fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('site.name', required=True)
        parser.add_argument('user.username', required=True)
        parser.add_argument('user.password', required=True, type=password)
        args = parser.parse_args()

        site_user = SiteUser()
        site_user.site = Site(name=args['site.name'])
        site_user.user = User(username=args['user.username'])
        site_user.user.hash_password(args['user.password'])

        session.add(site_user)
        session.commit()

        return site_user, 201
