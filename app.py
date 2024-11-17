from flask import Flask
from models import db
from routes import routes  # Import the main Blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:IRkIglOgceoetYigVBkQnXFgtVOtFHzX@junction.proxy.rlwy.net:42954/railway"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register the main Blueprint
app.register_blueprint(routes)

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)