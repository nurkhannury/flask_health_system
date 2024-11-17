from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Specialize, DiseaseType, Doctor

specialize = Blueprint('specialize', __name__, url_prefix='/specialize')

# List all specializations
@specialize.route('/')
def list_specialize():
    specializations = Specialize.query.all()
    return render_template('specialize.html', specializations=specializations)

# Add a specialization
@specialize.route('/add', methods=['GET', 'POST'])
def add_specialize():
    if request.method == 'POST':
        id = request.form['id']
        email = request.form['email']
        diseasetype = DiseaseType.query.get(id)
        doctor = Doctor.query.get(email)
        if diseasetype and doctor:
            new_specialization = Specialize(id=id, email=email)
            db.session.add(new_specialization)
            db.session.commit()
            return redirect(url_for('routes.specialize.list_specialize'))
        else:
            return "Invalid DiseaseType ID or Doctor email.", 400
    diseasetypes = DiseaseType.query.all()
    doctors = Doctor.query.all()
    return render_template('add_specialize.html', diseasetypes=diseasetypes, doctors=doctors)

# Delete a specialization
@specialize.route('/delete/<int:id>/<string:email>', methods=['POST'])
def delete_specialize(id, email):
    specialization = Specialize.query.get((id, email))
    db.session.delete(specialization)
    db.session.commit()
    return redirect(url_for('routes.specialize.list_specialize'))
