#!/usr/bin/python3
"""
contains class Customer
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship


class Customer(BaseModel, Base):
    """
    describes the customer table
    """

    __tablename__ = "customers"
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    phone_no = Column(String(60), nullable=False, unique=True)
    address = Column(String(256), nullable=False)
    email = Column(String(60), nullable=False, unique=True)
    phone_no_verify_status = Column(Boolean, default=False)
    reviews = relationship(
        "Review", backref="customer", cascade="all, delete, delete-orphan"
    )
    cart_items = relationship(
        "CartItem", backref="customer", cascade="all, delete, delete-orphan"
    )

    def __init__(self, *args, **kwargs):
        """initializes customer"""
        super().__init__(*args, **kwargs)
