from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Patients, Users

patients = Blueprint('patients', __name__)

# list all patients
@patients.route('/patients')
def list_patients():
    patients = Patients.query.all()
    return render_template('patients.html', patients=patients)

# add a new patient
@patients.route('/patients/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        email = request.form['email']
        user = Users.query.get(email)
        if user:
            new_patient = Patients(email=email)
            db.session.add(new_patient)
            db.session.commit()
            return redirect(url_for('routes.patients.list_patients'))
        return "User with the given email does not exist.", 400

    users = Users.query.all()
    return render_template('add_patient.html', users=users)

# delete a patient
@patients.route('/patients/delete/<string:email>', methods=['POST'])
def delete_patient(email):
    patient = Patients.query.get(email)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for('routes.patients.list_patients'))
