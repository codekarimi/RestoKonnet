#!/usr/bin/env python3
"""
This Module handles authtentication functions
"""
from os import getenv
from typing import Union
from .auth import Auth
from flask_mail import Message
from flask import url_for
from flask_mail import Mail
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from models import storage
from models.vendor import Vendor
from dotenv import load_dotenv
import secrets

load_dotenv()

mail = Mail()
SECRET_KEY = getenv("SECRET_KEY")

s = URLSafeTimedSerializer(SECRET_KEY)


def _hash_password(password: str) -> bytes:
    """Takes in a password string arguments and returns bytes"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _create_token() -> str:
    """Creates reset password token"""
    reset_token = secrets.SystemRandom().randrange(100000, 999999)
    return reset_token


class VendorAuth(Auth):
    """
    VendorAuth class to interact with the authentication database for the vendor user
    """

    def register_user(self, cls: Union[Vendor], **kwargs):
        """Regitsers a User"""
        email = kwargs.get("email")
        password = kwargs.get("password")
        try:
            user = storage.find_user_by(cls, email=email)
            if user:
                raise ValueError(f"Email {user.email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            kwargs["hashed_password"] = hashed_password.decode("utf-8")
            new_user = cls(**kwargs)
            return new_user

    def send_email_varification(self, email: str) -> str:
        """sends email varification"""

        token = s.dumps(email, salt="email-confirm")

        msg = Message(
            subject="Email Verification",
            sender="nwoghamichael3@gmail.com",
            recipients=[email],
        )

        confirmation_link = url_for(
            "app_views.verify_vendor_email", token=token, _external=True
        )

        msg.body = "Your Email Verification link is {}".format(confirmation_link)
        mail.send(msg)

        return confirmation_link

    def confirm_email(self, cls: Vendor, token: str) -> str:
        try:
            email = s.loads(token, salt="email-confirm", max_age=3600)
        except SignatureExpired:
            return None
        vendor = storage.find_user_by(cls, email=email)

        vendor.email_verify_status = True
        vendor.save()

        return vendor

    def creates_reset_password_token(self, cls: Union[Vendor], email: str) -> str:
        """Generates reset password token"""
        try:
            user = storage.find_user_by(cls, email=email)
        except Exception:
            raise ValueError
        reset_token = _create_token()
        try:
            storage.update_user(cls, user.id, reset_token=reset_token)
        except Exception:
            return None
        return reset_token

    def send_reset_password_token(self, email: str, reset_token: str) -> str:
        """sends reset password token to client"""

        msg = Message(
            subject="Email Verification",
            sender="nwoghamichael3@gmail.com",
            recipients=[email],
        )

        msg.body = f"Your Reset Password token {reset_token}"
        mail.send(msg)

        return reset_token
