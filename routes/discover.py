from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Discover, Country, Disease

discovers = Blueprint('discovers', __name__, url_prefix='/discovers')


# list all discover entries
@discovers.route('/')
def list_discovers():
    discovers = Discover.query.all()
    return render_template('discovers.html', discovers=discovers)


# add a new discover entry
@discovers.route('/add', methods=['GET', 'POST'])
def add_discover():
    if request.method == 'POST':
        cname = request.form['cname']
        disease_code = request.form['disease_code']
        first_enc_date = request.form['first_enc_date']

        new_discover = Discover(cname=cname, disease_code=disease_code, first_enc_date=first_enc_date)
        db.session.add(new_discover)
        db.session.commit()
        return redirect(url_for('routes.discovers.list_discovers'))

    countries = Country.query.all()
    diseases = Disease.query.all()
    return render_template('add_discover.html', countries=countries, diseases=diseases)


# delete a discover entry
@discovers.route('/delete/<string:cname>/<string:disease_code>', methods=['POST'])
def delete_discover(cname, disease_code):
    discover = Discover.query.get((cname, disease_code))
    db.session.delete(discover)
    db.session.commit()
    return redirect(url_for('routes.discovers.list_discovers'))
