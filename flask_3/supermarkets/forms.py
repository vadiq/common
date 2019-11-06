from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired, Length


class AddSupermarketForm(FlaskForm):
    supermarket_name = StringField('Name:', validators=[DataRequired(), Length(min=4, max=40)])
    supermarket_location = StringField('Location:', validators=[Length(max=100)])
    supermarket_image = FileField('Image:')
    submit = SubmitField('ADD')
