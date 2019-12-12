from flask import Flask
from random import _urandom

app = Flask(__name__)
app.secret_key = _urandom(256)

from app import routes