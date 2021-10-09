from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_url_path="/static")
    Bootstrap(app)
    return(app)

app = create_app()
CORS(app)

from app import views
