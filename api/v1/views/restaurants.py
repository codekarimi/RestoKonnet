#!/usr/bin/python3
"""
This Handles all the api Restful actions for Restaurants
"""
from flask import jsonify, request, make_response
from api.v1.views import app_views
from models import storage
from models.vendor import Vendor
from models.restaurant import Restaurant
from api.v1.errors import bad_request, not_found
from cloudinary.uploader import upload


@app_views.route("/restaurants", methods=["GET"], strict_slashes=False)
def get_restaurants():
    """This retrieves a list all restaurants"""

    restaurants_list = [rest.to_dict() for rest in storage.all(Restaurant).values()]
    return jsonify(restaurants_list)


@app_views.route("/restaurants/<restaurant_id>", methods=["GET"], strict_slashes=False)
def get_restaurant(restaurant_id):
    """This retrieves a restaurant based on its id"""

    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        return not_found("restaurant does not exist")
    return jsonify(restaurant.to_dict())


@app_views.route(
    "/vendors/<vendor_id>/restaurants", methods=["GET"], strict_slashes=False
)
def get_vendor_restaurant(vendor_id):
    """This retrieves a restaurant based on its id"""

    vendor = storage.get(Vendor, vendor_id)
    if not vendor:
        return not_found("vendor does not exist")
    if not vendor.restaurants:
        return jsonify({"message": "No Restaurant created yet"})
    return jsonify(vendor.restaurants.to_dict())


@app_views.route(
    "/vendors/<vendor_id>/restaurants", methods=["POST"], strict_slashes=False
)
def post_restaurant(vendor_id):
    """This creates a new restaurant object"""

    vendor = storage.get(Vendor, vendor_id)
    if not vendor:
        return not_found("vendor does not exist")

    if vendor.restaurants is not None:
        return bad_request("Vendor Already created Restaurant")

    form_request = request.form
    if not form_request:
        print("error 3")
        return bad_request("Not a form data")

    required = ["name", "address"]
    for val in required:
        if val not in form_request:
            return bad_request(f"Missing {val}")

    for rest in storage.all(Restaurant).values():
        if form_request["name"] == rest.name:
            return bad_request("Name Already Exist")

    print(request.files["image"])
    if request.files["image"]:
        image_path = request.files["image"]
        result = upload(image_path)

    restaurant = Restaurant(
        vendor_id=vendor_id,
        name=form_request["name"],
        address=form_request["address"],
        image=result["url"],
    )
    restaurant.save()

    return make_response(jsonify(restaurant.to_dict()), 201)


@app_views.route("/restaurants/<restaurant_id>", methods=["PUT"], strict_slashes=False)
def put_restaurant(restaurant_id):
    """Updates a particular restaurant's attributes"""

    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        return not_found("restaurant does not exist")

    form_request = request.form
    if not form_request:
        return bad_request("Not form-data")
    ignore_list = ["id", "updated_at", "created_at"]

    for key, value in form_request.items():
        if key not in ignore_list:
            setattr(restaurant, key, value)

    storage.save()
    return make_response(jsonify(restaurant.to_dict()), 201)


@app_views.route(
    "/restaurants/<restaurant_id>/image", methods=["PUT"], strict_slashes=False
)
def put_restaurant_image(restaurant_id):
    """Updates a particular restaurant's image"""

    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        return not_found("Restaurant does not exist")

    if "image" not in request.files:
        return bad_request("No image provided")

    image_path = request.files["image"]
    result = upload(image_path)
    setattr(restaurant, "image", result["url"])

    storage.save()
    return make_response(jsonify(restaurant.to_dict()), 201)


@app_views.route(
    "/restaurants/<restaurant_id>", methods=["DELETE"], strict_slashes=False
)
def delete_restaurant(restaurant_id):
    """Deletes a paticular restaurant object"""

    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        return not_found()

    storage.delete(restaurant)
    storage.save()

    return make_response(jsonify({}), 200)
