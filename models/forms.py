from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, PasswordField, EmailField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, length, NumberRange
from flask_wtf.file import FileField, FileRequired
from .tables import User


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=3)])
    email = EmailField('Email', validators=[DataRequired()])
    phone = IntegerField('phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), length(min=6)])
    submit = SubmitField('Create account')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired(), length(min=6)])
    new_password = PasswordField('New Password', validators=[DataRequired(), length(min=6)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), length(min=6)])
    change_password = SubmitField('Change Password')
