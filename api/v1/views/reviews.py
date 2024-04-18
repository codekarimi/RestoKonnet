#!/usr/bin/python3
"""
This Handles all the api Restful actions for Reviews
"""
from flask import jsonify, request, make_response
from api.v1.views import app_views
from models import storage
from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review
from api.v1.errors import error_response, bad_request, not_found


@app_views.route('/reviews', methods=['GET'], strict_slashes=False)
def get_reviews():
    """This retrieves a list all reviews"""

    reviews_list = [rev.to_dict() for rev in storage.all(Review).values()]
    return (reviews_list)


@app_views.route('restaurants/<restaurant_id>/reviews', methods=['GET'], strict_slashes=False)
def get_review(restaurant_id):
    """This retrieves a list all reviews of a particular restaurant"""

    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        return not_found("restaurant does not exist")
    reviews_list = [rev.to_dict() for rev in restaurant.reviews]
    return (reviews_list)


@app_views.route('restaurants/<restaurant_id>/reviews', methods=['POST'], strict_slashes=False)
def post_review(restaurant_id):
    """ This creates a new restaurant's review """

    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        return not_found("restaurant does not exist")
    
    form_request = request.form
    if not form_request:
        bad_request("Not a JSON")

    required = ['text', 'customer_id']
    for val in required:
        if val not in form_request:
            return bad_request(f"Missing {val}")

    if not storage.get(Customer, form_request['customer_id']):
        return not_found("customer does not exist")

    review = Review(restaurant_id=restaurant_id, **form_request)
    review.save()

    return make_response(jsonify(review.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def put_review(review_id):
    """Updates a particular restaurant's review attributes"""

    review = storage.get(Review, review_id)
    if not review:
        return not_found("review does not exist")

    form_request = request.form
    if not form_request:
        return bad_request("Not form-data")
    ignore_list = ['id', 'updated_at', 'created_at']

    for key, value in form_request.items():
        if key not in ignore_list:
            setattr(review, key, value)

    storage.save()
    return make_response(jsonify(review.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """Deletes a paticular review object """

    review = storage.get(Review, review_id)
    if not review:
        return not_found("review does not exist")
    
    storage.delete(review)
    storage.save()

    return make_response(jsonify({}), 200)
