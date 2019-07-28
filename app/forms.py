from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Employee

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class MenuItemEditForm(FlaskForm):
    itemnumber = IntegerField('Item Number', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    drinktype = StringField('Drink Type', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    submit = SubmitField('Update Item')

class AddOnEditForm(FlaskForm):
    addonnumber = IntegerField('Item Number', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    availability = BooleanField('Availability', validators=[DataRequired()])
    submit = SubmitField('Update Item')

class MenuItemAddForm(FlaskForm):
    itemnumber = IntegerField('Item Number', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    drinktype = StringField('Drink Type', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    submit = SubmitField('Add Item')

class AddOnAddForm(FlaskForm):
    addonnumber = IntegerField('Item Number', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    availability = BooleanField('Availability', validators=[DataRequired()])
    submit = SubmitField('Add Item')
