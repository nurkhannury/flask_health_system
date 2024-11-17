from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

# Import sub-blueprints
from .users import users
from .country import countries
from .patients import patients
from .diseasetypes import diseasetypes
from .diseases import diseases
from .discover import discovers
from .patientdisease import patientdisease
from .publicservants import publicservants  # Import PublicServants blueprint
from .doctors import doctors  # Import Doctors blueprint
from .specialize import specialize  # Import specialize
from .record import record  # Imp


routes.register_blueprint(users)
routes.register_blueprint(countries)
routes.register_blueprint(patients)
routes.register_blueprint(diseasetypes)
routes.register_blueprint(diseases)
routes.register_blueprint(discovers)
routes.register_blueprint(patientdisease)
routes.register_blueprint(publicservants)
routes.register_blueprint(doctors)
routes.register_blueprint(specialize)  # Register specialize
routes.register_blueprint(record)  # Register record

# Define the root route
@routes.route('/')
def home():
    return render_template('index.html')  # Render `index.html` template


