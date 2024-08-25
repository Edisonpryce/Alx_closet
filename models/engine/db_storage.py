from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from uuid import uuid4

usr = 'root'
pw = 'Password@5756'
host = 'localhost'
db = 'alxcloset'

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    telephone = Column(Integer(15), nullable=False)
    created_at = Column(String(128), nullable=True)
    updated_at = Column(String(128), nullable=True)


    def __init__(self, email, password, first_name, last_name, telephone):
        self.user_id = str(uuid4())
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        



engine = create_engine('mysql+pymysql://{usr}:{pw}@{host}/{db}')
session = Base.metadat.create_all(bind=engine)
Session = sessionmaker(bind=engine)
User()

