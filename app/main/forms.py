from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email_address = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Sign Up')