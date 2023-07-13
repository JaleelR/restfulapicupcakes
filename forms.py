
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField
from wtforms.validators import InputRequired, Optional, NumberRange, URL


class CupcakeFrom(FlaskForm):

    flavor = StringField("flavor", 
    validators=[InputRequired()])

    size = StringField("size", 
    validators=[InputRequired()])

    rating = FloatField("rating", 
    validators=[InputRequired(), NumberRange(max=10)])

    image = StringField("image", 
    validators=[Optional(), URL()])
  

