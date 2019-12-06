from flask import Flask, render_template, redirect, url_for, make_response
from app import app
from app.pets_class import Pet
from app.cart_class import Cart


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/pets")
def pets_view():
    pet_obj = Pet()
    pets_list = pet_obj.return_pets()

    return render_template("pets.html", pets_list=pets_list)


@app.route("/pet/<int:pet_id>")
def pet_view(pet_id):
    pet_obj = Pet()
    my_pet = pet_obj.return_pet(pet_id)
    return render_template("pet.html", my_pet=my_pet)


@app.route("/add_pet/<int:pet_id>")
def adding_to_cart(pet_id):
    cart_obj = Cart()
    cart_obj.add_to_cart(pet_id)
    return redirect(url_for('pets_view'))


@app.route("/cart")
def cart_view():
    return render_template("cart.html")