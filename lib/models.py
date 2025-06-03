from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cereals = relationship('Cereal', back_populates='supplier')

class Cereal(Base):
    __tablename__ = 'cereals'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    supplier = relationship('Supplier', back_populates='cereals')
    orders = relationship('Order', back_populates='cereal')

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    orders = relationship('Order', back_populates='customer')

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    cereal_id = Column(Integer, ForeignKey('cereals.id'))
    quantity = Column(Integer)
    total_price = Column(Float)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    customer = relationship('Customer', back_populates='orders')
    cereal = relationship('Cereal', back_populates='orders')

