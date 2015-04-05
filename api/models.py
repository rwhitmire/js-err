from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from passlib.apps import custom_app_context as pwd_context
from settings import SECRET_KEY
from db import session

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as TokenSerializer, BadSignature, SignatureExpired)

Base = declarative_base()


class Site(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    errors = relationship("Error")
    site_users = relationship("SiteUser")


class SiteUser(Base):
    __tablename__ = 'site_users'

    site_id = Column(Integer, ForeignKey('sites.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, index=True)
    password_hash = Column(String)
    site_users = relationship("SiteUser")

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


class Error(Base):
    __tablename__ = 'errors'

    id = Column(Integer, primary_key=True)
    site_id = Column(Integer, ForeignKey('sites.id'))
    message = Column(String)
    column = Column(Integer)
    line = Column(Integer)
    date = Column(DateTime)
    stack = Column(String)
    url = Column(String)
    app_code_name = Column(String)
    app_name = Column(String)
    app_version = Column(String)
    cookie_enabled = Column(Boolean)
    language = Column(String)
    platform = Column(String)
    product = Column(String)
    user_agent = Column(String)
    vendor = Column(String)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from settings import DB_URI
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    user = User(username='ryan')
    user.hash_password('password')

    session.add(user)
    session.commit()
