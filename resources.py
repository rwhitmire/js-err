from models import Error
from db import session

from flask.ext.restful import reqparse
from flask.ext.restful import Resource
from flask.ext.restful import fields
from flask.ext.restful import marshal_with

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
