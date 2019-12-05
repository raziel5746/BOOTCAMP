import wtforms
from wtforms.validators import data_required
import flask_wtf

class Form(flask_wtf.FlaskForm):
    name = wtforms.StringField('Name', validators=[data_required()])
    price = wtforms.StringField('Price', validators=[data_required()])
    category = wtforms.StringField('Category')
    stock = wtforms.StringField('Stock', validators=[data_required()])
    submit = wtforms.SubmitField('Add product')