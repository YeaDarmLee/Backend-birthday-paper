from flask_cors import CORS, cross_origin
from flask import Flask
import os

from .controller.LetterController import letter
from .controller.UserController import user

app = Flask(__name__)
CORS(app)
CORS(app, resources={r'*': {'origins': '*'}})

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app.config['SECRET_KEY'] = 'd9owj3982oi8329dsh38'

app.register_blueprint(letter)
app.register_blueprint(user)
