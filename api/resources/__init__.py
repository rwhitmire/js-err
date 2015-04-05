from flask import g
from flask.ext.httpauth import HTTPBasicAuth
from models.user import User
from db import session

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
