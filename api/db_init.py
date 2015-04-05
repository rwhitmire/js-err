from models.site import *
from models.error import *
from models.user import *
from db import session
from sqlalchemy import create_engine
from settings import DB_URI

engine = create_engine(DB_URI)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

user = User(username='ryan')
user.hash_password('password')

session.add(user)
session.commit()
