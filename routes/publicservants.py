from flask import Blueprint, render_template, request, redirect, url_for
from models import db, PublicServant, Users

publicservants = Blueprint('publicservants', __name__, url_prefix='/publicservants')

# list all public servants
@publicservants.route('/')
def list_publicservants():
    publicservants = PublicServant.query.all()
    return render_template('publicservants.html', publicservants=publicservants)

# add a new public servant
@publicservants.route('/add', methods=['GET', 'POST'])
def add_publicservant():
    if request.method == 'POST':
        email = request.form['email']
        department = request.form['department']
        user = Users.query.get(email)
        if user:
            new_publicservant = PublicServant(email=email, department=department)
            db.session.add(new_publicservant)
            db.session.commit()
            return redirect(url_for('routes.publicservants.list_publicservants'))
        return "User with the given email does not exist.", 400
    users = Users.query.all()
    return render_template('add_publicservant.html', users=users)

# delete a public servant
@publicservants.route('/delete/<string:email>', methods=['POST'])
def delete_publicservant(email):
    publicservant = PublicServant.query.get(email)
    db.session.delete(publicservant)
    db.session.commit()
    return redirect(url_for('routes.publicservants.list_publicservants'))
