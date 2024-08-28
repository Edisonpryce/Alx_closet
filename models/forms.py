from flask_wtf import FlaskForm
from wtforms import StringField, TelField, FloatField, PasswordField, EmailField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, Email, EqualTo
from flask_wtf.file import FileField, FileRequired

#from .tables import User


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4)])
    email = EmailField('Email', validators=[DataRequired()])
    phone = TelField('phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message="Password must be 6 min characters long")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Password must match")])
    submit = SubmitField('Create account')

    def validate_confirm_password(self, field):
        if  field.data != self.password.data:
            raise ValueError("Password must match")

"""
    def validate_email(self, field):
        if session.query(User.email).filter(User.email == field.data).scalar() is not None:
            raise ValueError("Email already exists")
    
    def validate_username(self, field):
        if session.query(User.username).filter(User.username == field.data).scalar() is not None:
            raise ValueError("Username already exists")
"""

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    



class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired(), Length(min=6)])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=6)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), Length(min=6)])
    change_password = SubmitField('Change Password')
