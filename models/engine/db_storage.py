from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

usr = 'root'
pw = 'Password@5756'
host = 'localhost'
db = 'alxcloset'

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    telephone = Column(Integer(12), nullable=False)





engine = create_engine('mysql+pymysql://{usr}:{pw}@{host}/{db}')

