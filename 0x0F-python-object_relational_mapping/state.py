#!/usr/bin/python3
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from user import Base, User
from sqlalchemy import Column, Integer, String

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address
"""
User.addresses = relationship("Address", order_by=Address.id, back_populates="user")"""
