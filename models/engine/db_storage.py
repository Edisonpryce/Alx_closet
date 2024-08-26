""" Using sqlalchemy to create database and tables
"""
from uuid import uuid4
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    # Columns
    user_id = Column(String(36), primary_key=True, nullable=False, default=lambda: str(uuid4()))
    email = Column(String(46), nullable=False)
    password = Column(String(150), nullable=False)
    first_name = Column(String(14), nullable=True)
    last_name = Column(String(14), nullable=True)
    telephone = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=True)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=True)



# Creation of the products table
class Product(Base):
    __tablename__ = 'product'

    id = Column(String(36), primary_key=True, nullable=False, default=lambda: str(uuid4()))
    product_name = Column(String(128), nullable=False)
    current_price = Column(Integer, nullable=False)
    chosen_price = Column(Integer, nullable=False)
    in_stock = Column(Integer, nullable=False)
    product_image = Column(String(128), nullable=True)
    created_at = Column(DateTime, default=datetime.now())



# Making of the cart table
class Cart(Base):
    __tablename__ = 'cart'

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)

    customer_link = Column(String(36), ForeignKey('user.id'), nullable=False)
    product_link = Column(String(36), ForeignKey('product.id'), nullable=False)
    
class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String(100), nullable=False)
    payment_id = Column(String(255), nullable=False)  # Adjusted length to a reasonable size

    customer_link = Column(String(36), ForeignKey('user.id'), nullable=False)
    product_link = Column(String(36), ForeignKey('product.id'), nullable=False)




usr = 'root'
pw = 'Password@5756'
host = 'localhost'
db = 'AlxCloset'
engine = create_engine('mysql+pymysql://{usr}:{pw}@{host}/{db}')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#session.add()
#session.commit()

