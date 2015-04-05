from models import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from passlib.apps import custom_app_context as pwd_context
from settings import SECRET_KEY
from db import session

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as TokenSerializer, BadSignature, SignatureExpired)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, index=True)
    password_hash = Column(String)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        serializer = TokenSerializer(SECRET_KEY, expires_in=expiration)
        return serializer.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        serializer = TokenSerializer(SECRET_KEY)
        try:
            data = serializer.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = session.query(User).get(data['id'])
        return user
