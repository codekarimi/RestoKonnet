#!/usr/bin/python3
"""
contains class CartItem
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey


class CartItem(BaseModel, Base):
    """
    describes the CartItem table
    """

    __tablename__ = "cart_items"
    customer_id = Column(String(60), ForeignKey("customers.id"))
    vendor_id = Column(String(60), ForeignKey("vendors.id"))
    restaurant_id = Column(String(60), ForeignKey("restaurants.id"), nullable=False)
    item_name = Column(String(60), nullable=False)
    item_price = Column(Integer, nullable=False)
    status = Column(String(60), default="pending")
    count = Column(Integer, default=1)

    def __init__(self, *args, **kwargs):
        """initializes orders"""
        super().__init__(*args, **kwargs)
