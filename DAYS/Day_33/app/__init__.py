from flask import Flask
from random import _urandom
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = _urandom(256)
app.config['DEBUG'] = True

# Database Connection
db_info = {'host': 'localhost',
           'database': 'bookstore',
           'psw': '',
           'user': 'postgres',
           'port': '5432'}

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgres://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
from app import routes
