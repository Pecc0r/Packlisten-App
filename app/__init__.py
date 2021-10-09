from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__, static_url_path="/static")
    Bootstrap(app)
    return(app)

app = create_app()

from app import views
