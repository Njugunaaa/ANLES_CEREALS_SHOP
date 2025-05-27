from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base



class Supplier(Base):
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    cereals = relationship("Cereal", back_populates="supplier")


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)



class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    cereal_id = Column(Integer, ForeignKey('cereal.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    cereal_ordered = relationship("Cereal", back_populates="order")
    customer = relationship("Customer", back_populates="orders")


class Cereal(Base):
    __tablename__ = 'cereal'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    order_id = Column(Integer, ForeignKey('order.id'))
    supplier_id = Column(Integer, ForeignKey('supplier.id'))

    order = relationship("Order", back_populates="cereal_ordered")
    supplier = relationship("Supplier", back_populates="cereals")