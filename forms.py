from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Optional


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])


class CreateRecipeForm(FlaskForm):
    recipe_name = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    health_labels = TextAreaField('Health Labels', validators=[Optional()])
    diet_labels = TextAreaField('Diet Labels', validators=[Optional()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    cooking_time = IntegerField('Cooking Time')
    serving_size = IntegerField('Serving Size')
    recipe_image = StringField('Copy Image Address Link', validators=[DataRequired()])
    source = StringField('Source URL Link', validators=[Optional()])