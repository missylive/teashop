from flask import render_template, flash, redirect
from app import app
from app import db
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import Employee, MenuItem

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
@app.route('/menu')
def menu():
    item_list = MenuItem.query.all()
    return render_template('menu.html', title='Menu', item_list=item_list)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    if form.validate_on_submit():
        employee = Employee.query.filter_by(employee_id=form.username.data).first()
        if employee is None or not employee.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(employee)
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')
