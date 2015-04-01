from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Error(Base):
    __tablename__ = 'errors'

    id = Column(Integer, primary_key=True)
    message = Column(String)
    column = Column(Integer)
    line = Column(Integer)
    date = Column(DateTime)
    stack = Column(String)
    url = Column(String)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from settings import DB_URI
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
