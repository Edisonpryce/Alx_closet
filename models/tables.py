""" Using sqlalchemy to create database tables
"""
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from bcrypt import hashpw, gensalt, checkpw
from flask_login import UserMixin

Base = declarative_base()

class User(Base, UserMixin):
    __tablename__ = 'users'

    # Columns for User infor intake 
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(26), nullable=False)
    email = Column(String(46), nullable=False, unique=True)
    password = Column(String(150), nullable=False)
    telephone = Column(String(15), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=True)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=True)
    cart_item = relationship("Cart", backref="user")
    order_item = relationship("Order", backref="user")


    def get_id(self):
        return str(self.id)
    
    def hash_password(self, password):
        hashed_password = hashpw(password.encode(), gensalt())
        return hashed_password

    def verify_password(self, input_password, stored_hash):
        if isinstance(stored_hash, str):
            stored_hash = stored_hash.encode('utf-8')
        return checkpw(input_password.encode(), stored_hash)
    
    def __str__(self):
     return f"<User {self.id}>"

class Product(Base):
    __tablename__ = 'products'

    # Creation of the products table
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(36), nullable=False)
    gender = Column(String(6), default='male', nullable=False)
    min_price = Column(Integer, nullable=False)
    max_price = Column(Integer, nullable=False)
    selected_price = Column(Integer, default=10, nullable=False)
    in_stock = Column(Integer, nullable=False)
    description = Column(String(200), nullable=False)
    product_picture = Column(String(2000), nullable=True)
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
    customer_link = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_link = Column(Integer, ForeignKey('products.id'), nullable=False)

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
    customer_link = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_link = Column(Integer, ForeignKey('products.id'), nullable=False)

    def __str__(self):
        return f"<Order {self.id}>"
    