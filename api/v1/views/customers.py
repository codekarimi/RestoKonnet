#!/usr/bin/python3
"""
This Handles all the api Restful actions for Customers
"""
from flask import jsonify, request, make_response
from api.v1.views import app_views
from models.customer import Customer
from models import storage
from flask_jwt_extended import jwt_required, get_jwt
from api.v1.customer_auth import CustomerAuth
from api.v1.errors import (
    error_response,
    forbidden_error,
    not_found,
    unauthorized_error,
    bad_request,
)

customer_auth = CustomerAuth()


@app_views.route("/customers/register", methods=["POST"], strict_slashes=False)
def register_customer():
    """
    This creates a new customer object
    """

    form_request = request.form

    if not form_request:
        return bad_request("Not form-data")

    required = ["first_name", "last_name", "phone_no", "address", "email"]
    for val in required:
        if val not in form_request:
            return bad_request(f"Missing {val}")
    try:
        customer = customer_auth.register_user(**form_request)
    except ValueError as error:
        return error_response(error)
    otp = customer_auth.sends_otp(customer.phone_no)
    if not otp:
        return error_response("failed to send otp")
    customer.otp = otp
    return make_response(jsonify(customer.to_dict()), 201)


@app_views.route("/customers/login", methods=["POST"], strict_slashes=False)
def login_customer():
    """
    Logs in a customer
    """

    form_request = request.form
    phone_no = form_request.get("phone_no")

    if not form_request:
        return bad_request("Not form-data")

    if "phone_no" not in form_request:
        return bad_request("phone_no missing")

    if not customer_auth.valid_login(phone_no):
        return unauthorized_error()

    otp = customer_auth.sends_otp(phone_no)
    # if not otp:
    #     return error_response(502, "Failed to generate otp")

    return (
        jsonify(
            {
                "Phone_no": phone_no,
                "OTP": otp,
            }
        ),
        200,
    )


@app_views.route("/customers/send_otp", methods=["POST"], strict_slashes=False)
def sends_otp():
    """sends otp for verification"""
    form_data = request.form

    if not form_data:
        error_response("Not form data")
    if "phone_no" not in form_data:
        bad_request("phone_no missing")

    phone_no = form_data.get("phone_no")

    otp = customer_auth.sends_otp(phone_no)

    if not otp:
        return error_response(502, "Failed to generate otp")
    return make_response(jsonify({"otp": otp, "meassge": "OTP Successfully sent!"}))


@app_views.route("/customers/verify_otp", methods=["POST"], strict_slashes=False)
def verify_phone_no_otp():
    """verify otp for a customers number"""

    form_data = request.form

    if not form_data:
        error_response("Not form data")

    required = ["otp", "phone_no"]
    for data in required:
        if data not in form_data:
            bad_request("otp missing")

    otp = form_data.get("otp")
    phone_no = form_data.get("phone_no")

    if not customer_auth.verify_otp(otp, phone_no):
        return bad_request("Wrong opt")

    access_token = customer_auth.create_session_token(phone_no)

    return make_response(
        jsonify({"message": "Phone Number Verified", "access_token": access_token})
    )


@app_views.route("/customers/logout", methods=["DELETE"], strict_slashes=False)
@jwt_required()
def logout_customer() -> str:
    """logs the user out"""
    access_token = get_jwt()["jti"]
    print(access_token)
    if access_token:
        customer_auth.destroy_session(access_token)
        return make_response(jsonify({"message": "successfully loggeout"}), 200)
    else:
        return forbidden_error()


@app_views.route("/customers", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_customers():
    """
    This retrieves a list all customers
    """
    customers_list = [cust.to_dict() for cust in storage.all(Customer).values()]
    return jsonify(customers_list)


@app_views.route("/customers/<customer_id>", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_customer(customer_id):
    """
    This retrieves a customer based on its id
    """
    customer = storage.get(Customer, customer_id)
    if not customer:
        return not_found("customer not found")
    return jsonify(customer.to_dict())


@app_views.route("/customers/<customer_id>", methods=["PUT"], strict_slashes=False)
@jwt_required()
def put_customer(customer_id):
    """
    Updates a particular customer's attributes
    """

    customer = storage.get(Customer, customer_id)
    if not customer:
        return not_found()
    form_request = request.form
    if not form_request:
        return bad_request("Not form-data")
    ignore_list = ["id", "updated_at", "created_at"]

    for key, value in form_request.items():
        if key not in ignore_list:
            setattr(customer, key, value)

    storage.save()
    return make_response(jsonify(customer.to_dict()), 200)


@app_views.route("/customers/<customer_id>", methods=["DELETE"], strict_slashes=False)
@jwt_required()
def delete_customer(customer_id):
    """
    Deletes a paticular customer object
    """

    customer = storage.get(Customer, customer_id)
    if not customer:
        return not_found()

    storage.delete(customer)
    storage.save()

    return make_response(jsonify({}), 200)
