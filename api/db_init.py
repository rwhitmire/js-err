from models.site import *
from models.error import *
from models.user import *
from models.site_user import *
from db import session
from sqlalchemy import create_engine
from settings import DB_URI

engine = create_engine(DB_URI)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

site_user = SiteUser()
site_user.site = Site(name='test site')
site_user.user = User(username='test')
site_user.user.hash_password('password')

session.add(site_user)
session.commit()
