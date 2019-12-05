from flask import Flask, render_template, render_template_string, redirect
import json
import random
import flask_wtf
import wtforms
from app import app
from app.forms import Form

PATH = app.config['DATA_PATH']

@app.route('/')
@app.route('/products')
def products():
    with open('app/db/products.db', 'r') as f:
        products = json.load(f)

    return render_template('products.html', products=products)


@app.route('/products/<product_id>')
def details(product_id):
    my_product = {}
    with open('app/db/products.db', 'r') as f:
        products = json.load(f)
    for product in products:
        print(type(product))
        if product['ProductId'] == product_id:
            my_product = product
            break
    return render_template('details.html', my_product=my_product)


@app.route('/add_product', methods=["GET","POST"])
def add_product():
    form = Form()

    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        category = form.category.data
        stock = form.stock.data

        with open('app/db/products.db', 'r') as f:
            products = json.load(f)
        print(products)
        new_product = {'Name': name, 'Price': price, 'Category': category, 'Stock': stock, 'ProductId': name}
    
        products.append(new_product)


        with open('app/db/products.db', 'w') as f:
            json.dump(products, f)  
            
        return redirect('/products')
    
    return render_template('add_product.html', form=form)