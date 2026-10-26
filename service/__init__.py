
from flask import Flask
from flask_talisman import Talisman


def create_app():
    app = Flask(__name__)

    Talisman(
        app,
        content_security_policy={
            "default-src": "'self'",
            "object-src": "'none'",
            "frame-ancestors": "'none'",
        },
    )

    return app
