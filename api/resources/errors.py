from flask.ext.restful import Resource
from flask.ext.restful import fields
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse
from resources import auth
from db import session
from models.error import Error


fields = {
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
    'cookie_enabled': fields.Boolean,
    'language': fields.String,
    'platform': fields.String,
    'product': fields.String,
    'user_agent': fields.String,
    'vendor': fields.String,
}


class ErrorsResource(Resource):
    @auth.login_required
    @marshal_with(fields)
    def get(self):
        return session.query(Error).all()

    @marshal_with(fields)
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
