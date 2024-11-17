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
from .publicservants import publicservants
from .doctors import doctors
from .specialize import specialize
from .record import record


# register sub-blueprints
routes.register_blueprint(users)
routes.register_blueprint(countries)
routes.register_blueprint(patients)
routes.register_blueprint(diseasetypes)
routes.register_blueprint(diseases)
routes.register_blueprint(discovers)
routes.register_blueprint(patientdisease)
routes.register_blueprint(publicservants)
routes.register_blueprint(doctors)
routes.register_blueprint(specialize)
routes.register_blueprint(record)

# define the root route
@routes.route('/')
def home():
    return render_template('index.html')


