from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, Length, NumberRange


class AddProductForm(FlaskForm):
    product_name = StringField('Name:', validators=[DataRequired(), Length(min=4, max=40)])
    product_description = StringField('Description:', validators=[Length(max=100)])
    product_price = IntegerField('Price:', validators=[DataRequired('please number here!'), NumberRange(min=0)])
    product_image = FileField('Image:')
    submit = SubmitField('ADD')
