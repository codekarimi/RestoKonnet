#!/usr/bin/python3
"""
contains class Item
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey


class Item(BaseModel, Base):
    """
    describes the items table
    """

    __tablename__ = "items"
    restaurant_id = Column(String(60), ForeignKey("restaurants.id"), nullable=False)
    name = Column(String(60), nullable=False)
    price = Column(Integer, nullable=False)
    image = Column(String(256), nullable=True)
    count = Column(Integer, default=1)

    def __init__(self, *args, **kwargs):
        """initializes item"""
        super().__init__(*args, **kwargs)
