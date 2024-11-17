from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Record, PublicServant, Country, Disease

record = Blueprint('record', __name__, url_prefix='/record')

# list all records
@record.route('/')
def list_record():
    records = Record.query.all()
    return render_template('record.html', records=records)

# add a record
@record.route('/add', methods=['GET', 'POST'])
def add_record():
    if request.method == 'POST':
        email = request.form['email']
        cname = request.form['cname']
        disease_code = request.form['disease_code']
        total_deaths = request.form['total_deaths']
        total_patients = request.form['total_patients']
        publicservant = PublicServant.query.get(email)
        country = Country.query.get(cname)
        disease = Disease.query.get(disease_code)
        if publicservant and country and disease:
            new_record = Record(email=email, cname=cname, disease_code=disease_code, total_deaths=total_deaths, total_patients=total_patients)
            db.session.add(new_record)
            db.session.commit()
            return redirect(url_for('routes.record.list_record'))
        else:
            return "Invalid email, country name, or disease code.", 400
    publicservants = PublicServant.query.all()
    countries = Country.query.all()
    diseases = Disease.query.all()
    return render_template('add_record.html', publicservants=publicservants, countries=countries, diseases=diseases)

# delete a record
@record.route('/delete/<string:email>/<string:cname>/<string:disease_code>', methods=['POST'])
def delete_record(email, cname, disease_code):
    record = Record.query.get((email, cname, disease_code))
    db.session.delete(record)
    db.session.commit()
    return redirect(url_for('routes.record.list_record'))
