from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(128), index=True, unique=True)
    phone = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))

    def __repr__(self):
        return '<Employee {}>'.format(self.employee_id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
