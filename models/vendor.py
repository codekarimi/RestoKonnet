#!/usr/bin/python3
"""
contains class Vendor
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship


class Vendor(BaseModel, Base):
    """
    describes the vendors table
    """

    __tablename__ = "vendors"
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    phone_no = Column(String(60), nullable=False)
    address = Column(String(256), nullable=False)
    hashed_password = Column(String(256), nullable=False)
    email = Column(String(60), nullable=False, unique=True)
    reset_token = Column(String(60))
    email_verify_status = Column(Boolean, default=False)

    restaurants = relationship(
        "Restaurant",
        backref="vendor",
        uselist=False,
        cascade="all, delete, delete-orphan",
    )
    cart_items = relationship(
        "CartItem", backref="vendor", cascade="all, delete, delete-orphan"
    )

    def __init__(self, *args, **kwargs):
        """initializes vendor"""
        super().__init__(*args, **kwargs)
