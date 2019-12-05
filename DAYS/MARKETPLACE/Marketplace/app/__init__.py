from flask import Flask, render_template, render_template_string, redirect
import json
import random
import flask_wtf
import wtforms

app = Flask(__name__)

app.config['SECRET_KEY'] = random._urandom(256)
app.config['DATA_PATH'] = 'static/products.db'

from app import routes, forms