from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    quantity = DecimalField('quantity', validators=[DataRequired()])
    unit = StringField('unit', validators=[DataRequired()])
    unit_price = DecimalField('unit_price', validators=[DataRequired()])


class ProductSaleForm(FlaskForm):
    quantity_sell = DecimalField('quantity', validators=[DataRequired()])