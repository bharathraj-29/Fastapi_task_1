from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, DateTime, CHAR
from sqlalchemy.orm import relationship
from database import base
import uuid

class User(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(CHAR(36), unique=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50))
    address = Column(String(100))
    email = Column(String(100))
    password = Column(String(200))
    ph_no = Column(BigInteger)
    role = Column(String(50))

    # item_id = Column(Integer, ForeignKey('items.id'))

    orders = relationship('Orders', back_populates='user')
    # items = relationship('Items', back_populates='owner')


class Items(base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    pro_id = Column(Integer)
    item_name = Column(String(50))
    product = Column(String(50))
    quan_and_qual = Column(String(50))
    price = Column(String(50))

    # user_id = Column(CHAR(36), ForeignKey('users.user_id'))

    ordered = relationship('Orders', back_populates='item')
    # owner = relationship('User', back_populates='items')


class Orders(base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(CHAR(36), ForeignKey('users.user_id'))
    item_id = Column(Integer, ForeignKey('items.id'))

    user = relationship('User', back_populates='orders')
    item= relationship('Items', back_populates='ordered')
    delivery = relationship('verify_otp', back_populates='deliver')

class verify_otp(base):
    __tablename__ = 'OTP'

    id = Column(Integer, primary_key=True, index=True)
    delivered = Column(String(50))
    otp = Column(Integer, nullable=True)
    otp_expiry = Column(DateTime, nullable=True)
    order_id = Column(Integer, ForeignKey("orders.id"))

    deliver = relationship('Orders',back_populates='delivery')


