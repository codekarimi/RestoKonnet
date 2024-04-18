#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import Base
from models.customer import Customer
from models.item import Item
from models.restaurant import Restaurant
from models.review import Review
from models.vendor import Vendor
from models.order import Order
from models.cart_item import CartItem
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import cloudinary
from dotenv import load_dotenv

from typing import Union, Dict


classes = {
    "Customer": Customer,
    "Item": Item,
    "Restaurant": Restaurant,
    "Review": Review,
    "Vendor": Vendor,
    "Order": Order,
    "CartItem": CartItem,
}


class DBStorage:
    """This class interacts with the MYSQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        load_dotenv()
        RESTO_POSTGRES_DB = getenv("RESTO_POSTGRES_DB")
        self.__engine = create_engine(RESTO_POSTGRES_DB)

        CLOUDINARY_CLOUD_NAME = getenv("CLOUDINARY_CLOUD_NAME")
        CLOUDINARY_API_KEY = getenv("CLOUDINARY_API_KEY")
        CLOUDINARY_API_SECRET = getenv("CLOUDINARY_API_SECRET")

        cloudinary.config(
            cloud_name=CLOUDINARY_CLOUD_NAME,
            api_key=CLOUDINARY_API_KEY,
            api_secret=CLOUDINARY_API_SECRET,
        )

    def all(
        self, cls: Union[Customer, Item, CartItem, Restaurant, Vendor, Order, Review]
    ) -> Dict:
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class
        and its ID, or None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        obj = next((value for value in all_cls.values() if value.id == id), None)
        return obj

    def count(self, cls=None):
        """
        Returns the number of objects in storage matching the given class
        If no class is passed, returns the count of all objects in storage
        """
        if not cls:
            return len(models.storage.all())
        else:
            return len(models.storage.all(cls))

    def find_user_by(
        self, cls: Union[Customer, Vendor], **kwargs
    ) -> Union[Customer, Vendor]:
        """returns the first row found in the users table as
        filtered by the method’s input arguments
        """
        if not kwargs:
            raise (InvalidRequestError)
        user = self.__session.query(cls).filter_by(**kwargs).first()
        if not user:
            raise (NoResultFound)
        return user

    def update_user(self, cls: Union[Customer, Vendor], cls_id: int, **kwargs) -> None:
        """update the user’s attributes as passed in the method’s
        arguments then commit changes to the database
        """
        user = self.find_user_by(cls, id=cls_id)

        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError
            setattr(user, key, value)

        self.__session.commit()
