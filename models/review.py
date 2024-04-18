#!/usr/bin/python3
"""
contains class Review
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """
    describes the reviews table
    """

    __tablename__ = "reviews"
    customer_id = Column(String(60), ForeignKey("customers.id"), nullable=False)
    restaurant_id = Column(String(60), ForeignKey("restaurants.id"), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)
