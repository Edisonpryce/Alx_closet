""" Using sqlalchemy to create database and tables
"""
from uuid import uuid4
from hashlib import md5
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    # Columns for User infor intake 
    id = Column(String(36), primary_key=True, nullable=False, default=lambda: str(uuid4()))
    email = Column(String(46), nullable=False)
    password = Column(String(150), nullable=False)
    username = Column(String(26), nullable=True)
    telephone = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=True)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=True)
    cart_item = relationship("Cart", backref="user")
    order_item = relationship("Order", backref="user")

    def __str__(self):
        return f"<User {self.id}>"


    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)


class Product(Base):
    __tablename__ = 'products'

    # Creation of the products table
    id = Column(String(36), primary_key=True, nullable=False, default=lambda: str(uuid4()))
    product_name = Column(String(36), nullable=False)
    current_price = Column(Integer, nullable=False)
    chosen_price = Column(Integer, nullable=False)
    in_stock = Column(Integer, nullable=False)
    product_image = Column(String(36), nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    carts = relationship("Cart", backref="product")
    orders = relationship("Order", backref="product")
    
    def __str__(self):
        return f"<Product {self.id}>"


class Cart(Base):
    __tablename__ = 'cart'

    # Making of the cart table
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)
    customer_link = Column(String(36), ForeignKey('users.id'), nullable=False)
    product_link = Column(String(36), ForeignKey('products.id'), nullable=False)

    def __str__(self):
        return f"<Cart {self.id}>"

    
class Order(Base):
    __tablename__ = 'orders'

    # Making of the orders table
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String(60), nullable=False)
    payment_id = Column(String(36), nullable=False) 
    customer_link = Column(String(36), ForeignKey('users.id'), nullable=False)
    product_link = Column(String(36), ForeignKey('products.id'), nullable=False)

    def __str__(self):
        return f"<Order {self.id}>"