from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/pets")
def pets_view():
    return render_template("pets.html")


@route("/pets/<pet_id>")
def pet_view(pet_id):
    return render_template("pet.html")


@route("/cart")
pass