from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DB_URL


db_engine = create_engine(DB_URL)
Session = sessionmaker(bind=db_engine)


def session_factory():
    Base.metadata.create_all(db_engine)
    return Session()


Base = declarative_base()


__all__ = ['Base', 'session_factory']