#!/usr/bin/python3
"""
This Handles all the api Restful actions for Reviews
"""
from flask import jsonify, request, make_response
from api.v1.views import app_views
from models import storage
from models.customer import Customer
from models.restaurant import Restaurant
from models.cart_item import CartItem
from models.vendor import Vendor
from api.v1.errors import error_response, bad_request, not_found


@app_views.route(
    "/restaurants/<restaurant_id>/cart_items", methods=["GET"], strict_slashes=False
)
def get_cart_item(restaurant_id):
    """
    Retrieves a list all cart_items in the cart of a particular restaurant
    """

    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        return not_found("restaurant does not exist")

    cart_items = []
    if request.args.get("customer_id"):
        customer_id = request.args.get("customer_id")
        customer = storage.get(Customer, customer_id)
        if customer:
            customer_cart = [cart.to_dict() for cart in customer.cart_items]
            print(customer_cart)
            resto_cart = [cart.to_dict() for cart in restaurant.cart_items]
            for cart in customer_cart:
                if cart in resto_cart:
                    cart_items.append(cart)
        else:
            return not_found("customer does not exist")

    elif request.args.get("vendor_id"):
        vendor_id = request.args.get("vendor_id")
        vendor = storage.get(Vendor, vendor_id)
        if vendor:
            vendor_cart = [cart.to_dict() for cart in vendor.cart_items]
            resto_cart = [cart.to_dict() for cart in restaurant.cart_items]
            for cart in vendor_cart:
                if cart in resto_cart:
                    cart_items.append(cart)
        else:
            return not_found("vendor does not exist")
    else:
        bad_request("NO vendor_id or customer_id")

    return cart_items


@app_views.route(
    "/restaurants/<restaurant_id>/cart_items", methods=["POST"], strict_slashes=False
)
def post_cutomer_item(restaurant_id):
    """This creates a new restaurant's cart_item"""

    restautant = storage.get(Restaurant, restaurant_id)
    if not restautant:
        return not_found("restaurant does not exist")

    form_request = request.form
    if not form_request:
        bad_request("Not a form data")

    required = ["item_name", "item_price"]
    for val in required:
        if val not in form_request:
            return bad_request(f"Missing {val}")

    cart_item = CartItem(restaurant_id=restaurant_id, **form_request)
    cart_item.save()

    return make_response(jsonify(cart_item.to_dict()), 201)


@app_views.route("/cart_items/<cart_item_id>", methods=["PUT"], strict_slashes=False)
def put_cart_item(cart_item_id):
    """Updates a particular customer cart_item attributes"""

    cart_item = storage.get(CartItem, cart_item_id)
    if not cart_item:
        return not_found("cart_item does not exist")

    form_request = request.form
    if not form_request:
        return bad_request("Not form-data")
    ignore_list = ["id", "updated_at", "created_at"]

    for key, value in form_request.items():
        if key not in ignore_list:
            setattr(order, key, value)

    storage.save()
    return make_response(jsonify(cart_item.to_dict()), 201)


@app_views.route("/cart_items/<cart_item_id>", methods=["DELETE"], strict_slashes=False)
def delete_cart_item(cart_item_id):
    """Deletes a paticular cart_item object"""

    cart_item = storage.get(CartItem, cart_item_id)
    if not cart_item:
        return not_found("cart_item does not exist")

    storage.delete(cart_item)
    storage.save()

    return make_response(jsonify({}), 200)
