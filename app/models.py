from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Employee(UserMixin, db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(128), index=True, unique=True)
    phone = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Employee {}>'.format(self.employee_id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return (self.employee_id)

@login.user_loader
def load_user(employee_id):
    return Employee.query.get(int(employee_id))

class MenuItem(db.Model):
    menu_item_number = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.String(128), index=True, unique=True)
    price = db.Column(db.Numeric)
    drinkstatus = db.Column(db.Boolean)
    drink_type = db.Column(db.String(128))
    drink_description = db.Column(db.String(128))

    def __repr__(self):
        return '<Menu Item {}>'.format(self.menu_item_number)
