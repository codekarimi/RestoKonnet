"""
This Handles all the api Restful actions for Vendors
"""

from flask import jsonify, request, make_response, redirect
from api.v1.views import app_views
from models.vendor import Vendor
from models import storage
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.orm.exc import NoResultFound
from api.v1.vendor_auth import VendorAuth
from dotenv import load_dotenv
from os import getenv
from api.v1.errors import (
    error_response,
    forbidden_error,
    not_found,
    unauthorized_error,
    bad_request,
)

vendor_auth = VendorAuth()

load_dotenv()
FRONTEND_BASE_URL = getenv("FRONTEND_BASE_URL")


@app_views.route("/vendors/register", methods=["POST"], strict_slashes=False)
def register_vendor():
    """This creates a new vendor object"""

    form_request = request.form

    if not form_request:
        return bad_request("Not form-data")

    required = ["first_name", "last_name", "address", "email", "password", "phone_no"]
    for val in required:
        if val not in form_request:
            return bad_request(f"Missing {val}")
    try:
        new_vendor = vendor_auth.register_user(Vendor, **form_request)
    except ValueError as error:
        return error_response(502, f"{error}")
    token = vendor_auth.send_email_varification(new_vendor.email)
    new_vendor.token = token
    new_vendor.save()
    return make_response(jsonify(new_vendor.to_dict()), 200)


@app_views.route("/vendors/login", methods=["POST"], strict_slashes=False)
def vendor_login():
    """This returns a token for an authenticated vendor"""

    form_request = request.form

    if not form_request:
        return bad_request("Not a form-data")

    required = ["email", "password"]
    for data in required:
        if data not in form_request:
            return bad_request(f"Missing {data}")

    email = form_request.get("email")
    password = form_request.get("password")

    if not vendor_auth.valid_login(Vendor, email, password):
        return unauthorized_error("Invalid Credentials")

    vendor = storage.find_user_by(Vendor, email=email)
    if vendor.email_verify_status is False:
        return unauthorized_error("Email not Verified")

    access_token = vendor_auth.create_session_token(Vendor, email)
    return (
        jsonify(
            {
                "vendor": vendor.to_dict(),
                "access_token": access_token,
                "message": "logged in",
            }
        ),
        200,
    )


@app_views.route("/vendors/email_verification", methods=["POST"], strict_slashes=False)
def sends_email_verification():
    """Sends email verification link"""
    form_request = request.form

    if not form_request:
        return bad_request("Not a form-data")

    if "email" not in form_request:
        return bad_request("Email missing")

    try:
        user = storage.find_user_by(Vendor, email=form_request.get("email"))
    except NoResultFound:
        return unauthorized_error("Invalid Email")

    confimation_link = vendor_auth.send_email_varification(user.email)
    return make_response(
        jsonify({"email": user.email, "confimation_link": confimation_link}), 200
    )


@app_views.route(
    "/vendors/verify_email/<token>", methods=["POST", "GET"], strict_slashes=False
)
def verify_vendor_email(token: str):
    """verifies the vendors email"""
    vendor = vendor_auth.confirm_email(Vendor, token)

    if not vendor:
        return error_response("Email Verification token expired")

    return redirect(f"{FRONTEND_BASE_URL}vendorSignIn")


@app_views.route("/vendors/logout", methods=["DELETE"], strict_slashes=False)
@jwt_required()
def logout_vendor() -> str:
    """logs the vendors out"""
    access_token = get_jwt()["jti"]
    if access_token:
        vendor_auth.destroy_session(access_token)
        return make_response(jsonify({"message": "successfully loggeout"}), 200)
    else:
        return forbidden_error()


@app_views.route("/vendors/reset_password", methods=["POST"], strict_slashes=False)
def gets_reset_password_token() -> str:
    """Gets reset password token"""
    form_data = request.form

    if not form_data:
        return bad_request("Not a form-data")

    if "email" not in form_data:
        return bad_request("Email missing")

    email = form_data.get("email")
    try:
        reset_token = vendor_auth.creates_reset_password_token(Vendor, email)
        vendor_auth.send_reset_password_token(email, reset_token)
    except Exception:
        return forbidden_error()
    return make_response(jsonify({"email": email, "reset_token": reset_token}), 201)


@app_views.route("/vendors/update_password", methods=["PUT"], strict_slashes=False)
def update_password() -> str:
    """Updates password"""

    form_data = request.form

    if not form_data:
        return bad_request("Not a form-data")

    email = form_data.get("email")
    new_password = form_data.get("new_password")
    reset_token = form_data.get("reset_token")

    required = ["email", "new_password", "reset_token"]

    for data in required:
        if data not in form_data.keys():
            return bad_request(f"{data} missing")
    try:
        vendor_auth.update_password(Vendor, reset_token, new_password)
    except Exception as error:
        print(error)
        return forbidden_error("User forbbiden")

    return make_response(jsonify({"email": email, "message": "Password updated"}), 201)


@app_views.route(
    "/vendors/sends_password_token", methods=["POST"], strict_slashes=False
)
def sends_password_token() -> str:
    """sends password token to client"""

    form_request = request.form

    if not form_request:
        return bad_request("Not a form-data")

    if "email" not in form_request:
        return bad_request("Email missing")

    email = form_request.get("email")
    try:
        reset_token = vendor_auth.creates_reset_password_token(email)
        vendor_auth.send_reset_password_token(email, reset_token)
    except Exception:
        return forbidden_error()

    vendor_auth.send_reset_password_token(email)
    return make_response(
        jsonify({"email": email, "reset_password_token": reset_token}),
        200,
    )


@app_views.route("/vendors", methods=["GET"], strict_slashes=False)
def get_vendors():
    """This retrieves a list all vendors"""

    vendors_list = [vendor.to_dict() for vendor in storage.all(Vendor).values()]
    return jsonify(vendors_list)


@app_views.route("/vendors/<vendor_id>", methods=["GET"], strict_slashes=False)
def get_vendor(vendor_id):
    """This retrieves a vendor based on its id"""

    vendor = storage.get(Vendor, vendor_id)
    if not vendor:
        return not_found("vendor does not exist")
    return jsonify(vendor.to_dict())


@app_views.route("/vendors/<vendor_id>", methods=["PUT"], strict_slashes=False)
def updates_vendor(vendor_id):
    """Updates a particular vendor's attributes"""

    vendor = storage.get(Vendor, vendor_id)
    if not vendor:
        return not_found()
    form_request = request.form
    if not form_request:
        return bad_request("Not form-data")
    ignore_list = ["id", "updated_at", "created_at"]

    for key, value in form_request.items():
        if key not in ignore_list:
            setattr(vendor, key, value)

    storage.save()
    return make_response(jsonify(vendor.to_dict()), 201)


@app_views.route("/vendors/<vendor_id>", methods=["DELETE"], strict_slashes=False)
def deletes_vendor(vendor_id):
    """Deletes a paticular vendor object"""

    vendor = storage.get(Vendor, vendor_id)
    if not vendor:
        return not_found("vendor does not exist")

    storage.delete(vendor)
    storage.save()

    return make_response(jsonify({}), 200)
