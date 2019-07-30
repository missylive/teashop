from flask import render_template, flash, redirect
from app import app
from app import db
from app.forms import LoginForm, MenuItemEditForm, MenuItemAddForm, AddOnEditForm, AddOnAddForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Employee, MenuItem, AddOnItem

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
@app.route('/menu')
def menu():
    item_list = MenuItem.query.all()
    return render_template('menu.html', title='Menu', item_list=item_list)
@app.route('/addonitem')
def addonitem():
    addon_list = AddOnItem.query.all()
    return render_template('addon.html', title='Menu', addon_list=addon_list)
@app.route('/mgmt', methods=['GET', 'POST'])
def mgmt():
    add_menu_form = MenuItemAddForm()
    add_addon_form = AddOnAddForm()
    if add_menu_form.validate_on_submit():
        add_item = MenuItem(menu_item_number=add_menu_form.itemnumber.data, item_name=add_menu_form.name.data, price=add_menu_form.price.data, drink_type=add_menu_form.drinktype.data, drink_description=add_menu_form.description.data)
        db.session.add(add_item)
        db.session.commit()
        flash('Menu item added successfully.')
        return redirect('/mgmt')
    if add_addon_form.validate_on_submit():
        add_item = AddOnItem(add_on_number=add_addon_form.addonnumber.data, food_description=add_addon_form.description.data, price=add_addon_form.price.data, foodstatus=add_addon_form.availability.data)
        db.session.add(add_item)
        db.session.commit()
        flash('Add on item added successfully.')
        return redirect('/mgmt')
    item_list = MenuItem.query.all()
    addon_list = AddOnItem.query.all()
    return render_template('mgmt.html', title='Management', item_list=item_list, addon_list=addon_list, add_menu_form=add_menu_form, add_addon_form=add_addon_form)
@app.route('/menu/<menu_item_number>', methods=['GET', 'POST'])
@login_required
def menuitem(menu_item_number):
    form = MenuItemEditForm()
    if form.validate_on_submit():
        edit_item = MenuItem.query.filter_by(menu_item_number=menu_item_number).first()
        edit_item.item_name = form.name.data
        edit_item.price = form.price.data
        edit_item.drink_type = form.drinktype.data
        edit_item.drink_description = form.description.data
        db.session.commit()
        flash('Menu item edited successfully.')
        return redirect('/mgmt')
    item_list = MenuItem.query.all()
    menu_item = MenuItem.query.filter_by(menu_item_number=menu_item_number).first_or_404()
    return render_template('mgmtmenu.html', menu_item=menu_item, item_list=item_list, form=form)
@app.route('/addon/<add_on_number>', methods=['GET', 'POST'])
@login_required
def addonitemmgmt(add_on_number):
    form = AddOnEditForm()
    if form.validate_on_submit():
        edit_item = AddOnItem.query.filter_by(add_on_number=add_on_number).first()
        edit_item.food_description = form.description.data
        edit_item.price = form.price.data
        edit_item.foodstatus = form.availability.data
        db.session.commit()
        flash('Add on item edited successfully.')
        return redirect('/mgmt')
    addon_list = AddOnItem.query.all()
    addon_item = AddOnItem.query.filter_by(add_on_number=add_on_number).first_or_404()
    return render_template('mgmtaddon.html', addon_list=addon_list, addon_item=addon_item, form=form)


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
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/index')
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(employee_id=form.userid.data, employee_name=form.name.data, phone=form.phone.data, password=form.password.data)
        employee.set_password(form.password.data)
        db.session.add(employee)
        db.session.commit()
        flash('Registration successful.')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)

@app.route('/deleteitem/<menu_item_number>')
def deleteitem(menu_item_number):
    menu_item = MenuItem.query.filter_by(menu_item_number=menu_item_number).first()
    db.session.delete(menu_item)
    db.session.commit()
    flash('Item deleted successfully.')
    return redirect('/mgmt')
@app.route('/deleteaddon/<add_on_number>')
def deleteaddon(add_on_number):
    addon_item = AddOnItem.query.filter_by(add_on_number=add_on_number).first()
    db.session.delete(addon_item)
    db.session.commit()
    flash('Item deleted successfully.')
    return redirect('/mgmt')
