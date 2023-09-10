from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):

    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String(45), nullable=False)
    password = Column(String(64),nullable=False)