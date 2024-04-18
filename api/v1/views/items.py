#!/usr/bin/python3
"""
This Handles all the api Restful actions for Items
"""
from flask import jsonify, request, make_response
from api.v1.views import app_views
from models import storage
from models.item import Item
from models.restaurant import Restaurant
from api.v1.errors import error_response, bad_request, not_found
from cloudinary.uploader import upload


@app_views.route('restaurants/<restaurant_id>/items', methods=['GET'], strict_slashes=False)
def get_item(restaurant_id):
    """This retrieves a list all items of a restaurant"""

    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        return not_found("restaurant does not exist")

    items_list = [item.to_dict() for item in restaurant.items]
    return (items_list)


@app_views.route('restaurants/<restaurant_id>/items', methods=['POST'], strict_slashes=False)
def post_item(restaurant_id):
    """ This creates a new restaurant's item """

    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        return not_found("restaurant does not exist")
    
    form_request = request.form
    if not form_request:
        bad_request("Not a form data")

    if request.files['image']:
        image_path = request.files['image']
        result = upload(image_path)

    required = ['name', 'price']
    for val in required:
        if val not in form_request:
            return bad_request(f"Missing {val}")

    item = Item(restaurant_id=restaurant_id, image=result['url'], name=form_request['name'], price=form_request['price'])
    item.save()

    return make_response(jsonify(item.to_dict()), 201)

@app_views.route('/items/<item_id>', methods=['PUT'], strict_slashes=False)
def put_item(item_id):
    """Updates a particular restaurant's item attributes"""

    item = storage.get(Item, item_id)
    if not item:
        return not_found("item does not exist")

    form_request = request.form
    if not form_request:
         return bad_request("Not Form-Data")
    ignore_list = ['id', 'updated_at', 'created_at']

    for key, value in form_request.items():
        if key not in ignore_list:
            setattr(item, key, value)

    storage.save()
    return make_response(jsonify(item.to_dict()), 201)

@app_views.route('/items/<item_id>/image', methods=['PUT'], strict_slashes=False)
def put_item_image(item_id):
    """Updates a particular restaurant's item image"""

    item = storage.get(Item, item_id)
    if not item:
        return not_found("item does not exist")

    if 'image' not in request.files:
        return bad_request('No image provided')
    
    image_path = request.files['image']
    result = upload(image_path)
    setattr(item, 'image', result['url'])

    storage.save()
    return make_response(jsonify(item.to_dict()), 201)

@app_views.route('/items/<item_id>', methods=['DELETE'], strict_slashes=False)
def delete_item(item_id):
    """Deletes a paticular restaurant object """

    item = storage.get(Item, item_id)
    if not item:
        return not_found("item does not exist")
    
    storage.delete(item)
    storage.save()

    return make_response(jsonify({}), 200)
