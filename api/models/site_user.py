from models import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class SiteUser(Base):
    __tablename__ = 'site_users'

    site_id = Column(Integer, ForeignKey('sites.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user = relationship('User', backref='site_users')
    site = relationship('Site', backref='site_users')
