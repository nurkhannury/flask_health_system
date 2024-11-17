from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# setting classes for each table in the database to ensure connection
class Users(db.Model):
    email = db.Column(db.String(60), primary_key=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(40))
    salary = db.Column(db.Integer)
    phone = db.Column(db.String(20))

class Country(db.Model):
    cname = db.Column(db.String(50), primary_key=True)
    population = db.Column(db.BigInteger)

class Patients(db.Model):
    email = db.Column(db.String(60), db.ForeignKey('users.email', ondelete="CASCADE"), primary_key=True)

class DiseaseType(db.Model):
    __tablename__ = 'diseasetype'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(140))



class Disease(db.Model):
    __tablename__ = 'disease'
    disease_code = db.Column(db.String(50), primary_key=True)
    pathogen = db.Column(db.String(20))
    description = db.Column(db.String(140))
    id = db.Column(db.Integer, db.ForeignKey('diseasetype.id', ondelete="CASCADE"))
    disease_type = db.relationship('DiseaseType', backref=db.backref('diseases', cascade="all, delete-orphan"))

class Discover(db.Model):
    cname = db.Column(db.String(50), db.ForeignKey('country.cname'), primary_key=True)
    disease_code = db.Column(db.String(50), db.ForeignKey('disease.disease_code'), primary_key=True)
    first_enc_date = db.Column(db.Date)

class PatientDisease(db.Model):
    __tablename__ = 'patientdisease'
    email = db.Column(db.String(60), db.ForeignKey('users.email', ondelete="CASCADE"), primary_key=True)
    disease_code = db.Column(db.String(50), db.ForeignKey('disease.disease_code', ondelete="CASCADE"), primary_key=True)

class PublicServant(db.Model):
    __tablename__ = 'publicservant'
    email = db.Column(db.String(60), db.ForeignKey('users.email', ondelete="CASCADE"), primary_key=True)
    department = db.Column(db.String(50), nullable=False)


class Doctor(db.Model):
    __tablename__ = 'doctor'
    email = db.Column(db.String(60), db.ForeignKey('users.email', ondelete="CASCADE"), primary_key=True)
    degree = db.Column(db.String(20), nullable=False)

class Specialize(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('diseasetype.id', ondelete="CASCADE"), primary_key=True)
    email = db.Column(db.String(60), db.ForeignKey('doctor.email', ondelete="CASCADE"), primary_key=True)

class Record(db.Model):
    email = db.Column(db.String(60), db.ForeignKey('publicservant.email', ondelete="CASCADE"), primary_key=True)
    cname = db.Column(db.String(50), db.ForeignKey('country.cname', ondelete="CASCADE"), primary_key=True)
    disease_code = db.Column(db.String(50), db.ForeignKey('disease.disease_code', ondelete="CASCADE"), primary_key=True)
    total_deaths = db.Column(db.Integer)
    total_patients = db.Column(db.Integer)
