#!/usr/bin/python3
"""
contains class Order
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, JSON


class Order(BaseModel, Base):
    """
    describes the orders table
    """
    __tablename__ = 'orders'
    restaurant_id = Column(String(60), ForeignKey('restaurants.id'), nullable=False)
    items = Column(JSON, nullable=False)
    customer = Column(JSON, nullable=False)
    total_amount = Column(Integer, nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes orders"""
        super().__init__(*args, **kwargs)
