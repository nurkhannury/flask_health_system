from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Users

users = Blueprint('users', __name__, url_prefix='/users')  # Add `url_prefix`

# List all users
@users.route('/')
def list_users():
    users = Users.query.all()
    return render_template('users.html', users=users)

# Add a new user
@users.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        surname = request.form['surname']
        salary = request.form['salary']
        phone = request.form['phone']
        new_user = Users(email=email, name=name, surname=surname, salary=salary, phone=phone)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('routes.users.list_users'))  # Reference Blueprint endpoint directly
    return render_template('add_user.html')

# Edit a user
@users.route('/edit/<string:email>', methods=['GET', 'POST'])
def edit_user(email):
    user = Users.query.get(email)
    if request.method == 'POST':
        user.name = request.form['name']
        user.surname = request.form['surname']
        user.salary = request.form['salary']
        user.phone = request.form['phone']
        db.session.commit()
        return redirect(url_for('routes.users.list_users'))  # Reference Blueprint endpoint directly
    return render_template('edit_user.html', user=user)

# Delete a user
@users.route('/delete/<string:email>', methods=['POST'])
def delete_user(email):
    user = Users.query.get(email)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('routes.users.list_users'))  # Reference Blueprint endpoint directly
