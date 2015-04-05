from models import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import Boolean


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
