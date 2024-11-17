from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Country

countries = Blueprint('countries', __name__)

# list all countries
@countries.route('/countries')
def list_countries():
    countries = Country.query.all()
    return render_template('countries.html', countries=countries)

# add a new country
@countries.route('/countries/add', methods=['GET', 'POST'])
def add_country():
    if request.method == 'POST':
        cname = request.form['cname']
        population = request.form['population']
        new_country = Country(cname=cname, population=population)
        db.session.add(new_country)
        db.session.commit()
        return redirect(url_for('routes.countries.list_countries'))
    return render_template('add_country.html')

# delete a country
@countries.route('/countries/delete/<string:cname>', methods=['POST'])
def delete_country(cname):
    country = Country.query.get(cname)
    db.session.delete(country)
    db.session.commit()
    return redirect(url_for('routes.countries.list_countries'))
