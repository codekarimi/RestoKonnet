#!/usr/bin/python3
"""
This Handles all the api Restful actions for Reviews
"""
from flask import jsonify, request, make_response
from api.v1.views import app_views
from models import storage
from models.customer import Customer
from models.restaurant import Restaurant
from models.order import Order
from api.v1.errors import error_response, bad_request, not_found


@app_views.route('/orders', methods=['GET'], strict_slashes=False)
def get_orders():
    """This retrieves a list all orders"""

    orders_list = [order.to_dict() for order in storage.all(Order).values()]
    return (orders_list)


@app_views.route('restaurants/<restaurant_id>/orders', methods=['GET'], strict_slashes=False)
def get_restaurant_order(restaurant_id):
    """This retrieves a list all orders of a particular restaurant"""

    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        return not_found("restaurant does not exist")
    orders_list = [order.to_dict() for order in restaurant.orders]
    return (orders_list)

# @app_views.route('customers/<customer_id>/orders', methods=['GET'], strict_slashes=False)
# def get_customer_order(customer_id):
#     """This retrieves a list all orders of a particular customer"""

#     customer = storage.get(Customer, customer_id)
#     if not customer:
#         return not_found("customer does not exist")
#     orders_list = [order.to_dict() for order in customer.orders]
#     return (orders_list)


@app_views.route('restaurants/<restaurant_id>/orders', methods=['POST'], strict_slashes=False)
def post_order(restaurant_id):
    """ This creates a new restaurant's order """

    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        return not_found("restaurant does not exist")
    
    json_request = request.get_json()
    if not json_request:
        bad_request("Not a JSON")

    required = ['items', 'total_amount', 'customer']
    for val in required:
        if val not in json_request:
            return bad_request(f"Missing {val}")

    items = json_request.get('items')
    customer = json_request.get('customer')
    total_amount = json_request.get('total_amount')

    # For demonstration, just assuming the order is created and returning a response

    order = Order(restaurant_id=restaurant_id,
                    items=items,
                    customer=customer,
                    total_amount=total_amount
        )
    order.save()
    return make_response(jsonify(order.to_dict()), 201)


# @app_views.route('/orders/<order_id>', methods=['PUT'], strict_slashes=False)
# def put_order(order_id):
#     """Updates a particular restaurant's order attributes"""

#     order = storage.get(Order, order_id)
#     if not order:
#         return not_found("order does not exist")

#     form_request = request.form
#     if not form_request:
#         return bad_request("Not form-data")
#     ignore_list = ['id', 'updated_at', 'created_at']

#     for key, value in form_request.items():
#         if key not in ignore_list:
#             setattr(order, key, value)

#     storage.save()
#     return make_response(jsonify(order.to_dict()), 201)


@app_views.route('/orders/<order_id>', methods=['DELETE'], strict_slashes=False)
def delete_order(order_id):
    """Deletes a paticular order object """

    order = storage.get(Order, order_id)
    if not order:
        return not_found("order does not exist")
    
    storage.delete(order)
    storage.save()

    return make_response(jsonify({}), 200)
