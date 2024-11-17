from flask import Blueprint, render_template, request, redirect, url_for
from models import db, DiseaseType

diseasetypes = Blueprint('diseasetypes', __name__, url_prefix='/diseasetypes')

# List all disease types
@diseasetypes.route('/')
def list_diseasetypes():
    diseasetypes = DiseaseType.query.all()
    return render_template('diseasetypes.html', diseasetypes=diseasetypes)

# Add a new disease type
@diseasetypes.route('/add', methods=['GET', 'POST'])
def add_diseasetype():
    if request.method == 'POST':
        id = request.form['id']
        description = request.form['description']

        # Ensure the ID is unique
        if DiseaseType.query.get(id):
            return "DiseaseType with this ID already exists.", 400

        new_diseasetype = DiseaseType(id=id, description=description)
        db.session.add(new_diseasetype)
        db.session.commit()
        return redirect(url_for('routes.diseasetypes.list_diseasetypes'))
    return render_template('add_diseasetype.html')



# Delete a disease type
@diseasetypes.route('/delete/<int:id>', methods=['POST'])
def delete_diseasetype(id):
    diseasetype = DiseaseType.query.get(id)
    db.session.delete(diseasetype)
    db.session.commit()
    return redirect(url_for('routes.diseasetypes.list_diseasetypes'))
