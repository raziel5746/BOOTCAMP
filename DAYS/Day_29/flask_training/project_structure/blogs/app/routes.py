import flask
from app import app

@app.route("/")
def index():
    posts=[
        {"author":"Eyal", "body":"I love python"},
        {"author":"Fish", "body":"I love water"},
        {"author":"Herpetolog", "body":"I love pythons"},
    ]
    return flask.render_template(posts=posts)