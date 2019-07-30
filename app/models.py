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

class AddOnItem(db.Model):
    add_on_number = db.Column(db.Integer, primary_key = True)
    food_description = db.Column(db.String(128))
    price = db.Column(db.Numeric)
    foodstatus = db.Column(db.Boolean)

    def __repr__(self):
        return '<Add On Item {}>'.format(self.add_on_number)

class DrinkOrder(db.Model):
    order_number = db.Column(db.Integer, primary_key = True)
    menu_items = db.relationship('OrderItem', backref='drinkorder', lazy=True)
#    addon_items = db.relationship('OrderItem', backref='drinkorder', lazy=True)
    order_time = db.Column(db.DateTime)
    order_date = db.Column(db.DateTime)
    order_type = db.Column(db.String(128))
    discount = db.Column(db.Numeric)
    tax = db.Column(db.Numeric)
    tips = db.Column(db.Numeric)
    notes = db.Column(db.String(128))

class OrderItem(db.Model):
    order_number = db.Column(db.Integer, db.ForeignKey('drink_order.order_number'), nullable=False, primary_key = True)
#    menu_item_number = db.Column(db.Integer, db.ForeignKey('menu_item.menu_item_number'), nullable=False, primary_key = True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id'), nullable=False)
    add_on_number = db.Column(db.Integer, db.ForeignKey('add_on_item.add_on_number'), nullable=True)
    menu_item_name = db.Column(db.String(128), db.ForeignKey('menu_item.item_name'), nullable=False, primary_key = True)
    def __repr__(self):
        return self.menu_item_name
