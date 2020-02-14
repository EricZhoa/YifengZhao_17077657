from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email_address = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email_address(self, email_address):
        user = User.query.filter_by(email=email_address.data).first()
        if user is not None:
            raise ValidationError(
                'An account is already registered for that email address. Please use a different email address.')
