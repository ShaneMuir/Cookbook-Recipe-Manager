from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Sign In')
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Register')

