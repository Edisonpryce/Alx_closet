from flask_wtf import FlaskForm
from wtforms import StringField, TelField, FloatField, PasswordField, EmailField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Email, EqualTo
from flask_wtf.file import FileField, FileRequired


class SignUpForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=4)])
    email = EmailField('Email', validators=[DataRequired()])
    phone = TelField('phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message="Password must be 6 min characters long")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Password must match")])
    submit = SubmitField('Create account')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    

class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired(), Length(min=6)])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=6)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), Length(min=6)])
    change_password = SubmitField('Change Password')

class AdminPrivilagesForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Update')

class ShopItemsForm(FlaskForm):
    product_name = StringField('Name of Product', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    min_price = FloatField('minimum Price', validators=[DataRequired()])
    max_price = FloatField('maximum  Price', validators=[DataRequired()])
    in_stock = IntegerField('In Stock', validators=[DataRequired(), NumberRange(min=0)])
    selected_price = IntegerField('Selected Price', validators=[DataRequired()])
    product_picture = FileField('Product Picture', validators=[FileRequired()])
    description = StringField('Description', validators=[DataRequired()])
    
    add_product = SubmitField('Add Product')
    update_product = SubmitField('Update')


class OrderForm(FlaskForm):
    order_status = SelectField('Order Status', choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'),
                                                        ('Out for delivery', 'Out for delivery'),
                                                        ('Delivered', 'Delivered'), ('Canceled', 'Canceled')])
