from flask import Flask, render_template, render_template_string, redirect, url_for
import json
import flask_wtf
import wtforms
from wtforms.validators import data_required, Length, ValidationError
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(16)


def category_check(message=None):
    message = "You can't create a new category."

    def _validate_name(form, field):
        with open('data.json', 'r') as f:
            keys = list(json.load(f).keys())

        if field.data not in keys:
            raise wtforms.ValidationError(message)

    return _validate_name


class Form(flask_wtf.FlaskForm):

    name = wtforms.StringField('Particle name', validators=[data_required(), Length(min=2, max=25, message='Particle name too short or too long (2 chars min, 25 chars max.)')])
    category = wtforms.StringField('Particle category', validators=[data_required(), category_check()])
    submit = wtforms.SubmitField('Submit new particle')



@app.route('/realm/<realm>')
def realm_index(realm):
    return render_template('realm.html', realm=realm)


@app.route('/particles')
def particles_view():

    with open('data.json', 'r') as f:
        data = json.load(f)
    return render_template('particles.html', particles=data)

@app.route('/')
@app.route('/form', methods=['GET', 'POST'])
def add_particle():
    form = Form()

    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data

        with open('data.json', 'r') as f:
            data = json.load(f)
        data[category].append(name)
        return render_template('particles.html', form=form)
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

