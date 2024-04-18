from os import getenv


class Config(object):
    SECRET_KEY = getenv("SECRET_KEY")
    JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")
    MAIL_SERVER = getenv("MAIL_SERVER")
    MAIL_USERNAME = getenv("MAIL_USERNAME")
    MAIL_PASSWORD = getenv("MAIL_PASSWORD")
    MAIL_PORT = getenv("MAIL_PORT")
    MAIL_USE_SSL = getenv("MAIL_USE_SSL")
