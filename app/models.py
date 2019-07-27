from app import db

class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(128), index=True, unique=True)
    phone = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))

    def __repr__(self):
        return '<Employee {}>'.format(self.employee_id)
