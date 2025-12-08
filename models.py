from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, DateTime, CHAR
from sqlalchemy.orm import relationship
from database import base
import uuid

class Role(base):
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(50),unique=True)

    users = relationship("User", back_populates="role")

class User(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(CHAR(36), unique=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50))
    address = Column(String(100))
    email = Column(String(100), unique = True)
    password = Column(String(200))
    ph_no = Column(BigInteger)

    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role", back_populates="users")

    # item_id = Column(Integer, ForeignKey('items.id'))

    orders = relationship('Orders', back_populates='user')
    # items = relationship('Items', back_populates='owner')


class Items(base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    pro_id = Column(Integer)
    item_name = Column(String(50))
    product = Column(String(50))
    quantity = Column(String(50))
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



