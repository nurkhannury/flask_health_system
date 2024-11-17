from flask import Blueprint, render_template, request, redirect, url_for
from models import db, PatientDisease, Users, Disease

patientdisease = Blueprint('patientdisease', __name__, url_prefix='/patientdisease')

# list all patient diseases
@patientdisease.route('/')
def list_patientdisease():
    patientdiseases = PatientDisease.query.all()
    return render_template('patientdisease.html', patientdiseases=patientdiseases)

# add a new patient disease
@patientdisease.route('/add', methods=['GET', 'POST'])
def add_patientdisease():
    if request.method == 'POST':
        email = request.form['email']
        disease_code = request.form['disease_code']
        user = Users.query.get(email)
        disease = Disease.query.get(disease_code)
        if user and disease:
            new_record = PatientDisease(email=email, disease_code=disease_code)
            db.session.add(new_record)
            db.session.commit()
            return redirect(url_for('routes.patientdisease.list_patientdisease'))
        else:
            return "Invalid email or disease code.", 400
    users = Users.query.all()
    diseases = Disease.query.all()
    return render_template('add_patientdisease.html', users=users, diseases=diseases)

# delete a patient disease
@patientdisease.route('/delete/<string:email>/<string:disease_code>', methods=['POST'])
def delete_patientdisease(email, disease_code):
    record = PatientDisease.query.get((email, disease_code))
    db.session.delete(record)
    db.session.commit()
    return redirect(url_for('routes.patientdisease.list_patientdisease'))
