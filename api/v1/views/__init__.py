#!/usr/bin/python3
from flask import Blueprint
from os import getenv


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.customers import *
from api.v1.views.vendors import *
from api.v1.views.restaurants import *
from api.v1.views.items import *
from api.v1.views.reviews import *
from api.v1.views.orders import *
from api.v1.views.cart_items import *
