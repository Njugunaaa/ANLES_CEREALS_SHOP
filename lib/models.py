from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class Supplier(Base):
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cereals = relationship("Cereal", back_populates="supplier")

class Cereal(Base):
    __tablename__ = 'cereal'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    supplier_id = Column(Integer, ForeignKey('supplier.id'))

    supplier = relationship("Supplier", back_populates="cereals")
    orders = relationship("Order", back_populates="cereal")

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    orders = relationship("Order", back_populates="customer")

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    cereal_id = Column(Integer, ForeignKey('cereal.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))
    quantity = Column(Integer)
    status = Column(String, default="pending")
    total_price = Column(Float) 
    created_at = Column(DateTime, default=datetime.utcnow)

    cereal = relationship("Cereal", back_populates="orders")
    customer = relationship("Customer", back_populates="orders")
