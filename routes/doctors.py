from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Doctor, Users

doctors = Blueprint('doctors', __name__, url_prefix='/doctors')

# list all doctors
@doctors.route('/')
def list_doctors():
    doctors = Doctor.query.all()
    return render_template('doctors.html', doctors=doctors)

# add a new doctor
@doctors.route('/add', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        email = request.form['email']
        degree = request.form['degree']
        user = Users.query.get(email)
        if user:
            new_doctor = Doctor(email=email, degree=degree)
            db.session.add(new_doctor)
            db.session.commit()
            return redirect(url_for('routes.doctors.list_doctors'))
        return "User with the given email does not exist.", 400
    users = Users.query.all()
    return render_template('add_doctor.html', users=users)

# delete a doctor
@doctors.route('/delete/<string:email>', methods=['POST'])
def delete_doctor(email):
    doctor = Doctor.query.get(email)
    db.session.delete(doctor)
    db.session.commit()
    return redirect(url_for('routes.doctors.list_doctors'))
