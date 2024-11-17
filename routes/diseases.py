from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Disease, DiseaseType

diseases = Blueprint('diseases', __name__, url_prefix='/diseases')

# List all diseases
@diseases.route('/')
def list_diseases():
    diseases = Disease.query.all()
    return render_template('diseases.html', diseases=diseases)

# Add a new disease
@diseases.route('/add', methods=['GET', 'POST'])
def add_disease():
    if request.method == 'POST':
        disease_code = request.form['disease_code']
        pathogen = request.form['pathogen']
        description = request.form['description']
        id = request.form['id']
        diseasetype = DiseaseType.query.get(id)
        if diseasetype:
            new_disease = Disease(disease_code=disease_code, pathogen=pathogen, description=description, id=id)
            db.session.add(new_disease)
            db.session.commit()
            return redirect(url_for('routes.diseases.list_diseases'))
        return "Invalid DiseaseType ID", 400
    diseasetypes = DiseaseType.query.all()
    return render_template('add_disease.html', diseasetypes=diseasetypes)

# Delete a disease
@diseases.route('/delete/<string:disease_code>', methods=['POST'])
def delete_disease(disease_code):
    disease = Disease.query.get(disease_code)
    db.session.delete(disease)
    db.session.commit()
    return redirect(url_for('routes.diseases.list_diseases'))
