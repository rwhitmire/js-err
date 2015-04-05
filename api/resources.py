from models.error import Error
from models.user import User
from db import session

from flask import g
from flask.ext.restful import reqparse
from flask.ext.restful import Resource
from flask.ext.restful import fields
from flask.ext.restful import marshal_with
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()












