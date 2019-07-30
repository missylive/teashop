from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Employee

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    userid = StringField('User ID', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
            'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_userid(self, userid):
        user = Employee.query.filter_by(employee_id=userid.data).first()
        if user is not None:
            raise ValidationError('Please choose a different user ID.')



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
