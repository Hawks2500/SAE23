from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
  return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81)


class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  formation = db.Column(db.String(100), nullable=False)
  group = db.Column(db.String(10), nullable=False)
  sub_group = db.Column(db.String(10), nullable=False)
  vehicles = db.relationship('Vehicle', backref='owner', lazy=True)


class Vehicle(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  student_id = db.Column(db.Integer,
                         db.ForeignKey('student.id'),
                         nullable=False)
  vehicle_type = db.Column(db.String(50), nullable=False, default='pied')
  seats = db.Column(db.Integer, nullable=True)
  license_plate = db.Column(db.String(10), nullable=True)


class Location(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  student_id = db.Column(db.Integer,
                         db.ForeignKey('student.id'),
                         nullable=False)
  location_type = db.Column(
    db.String(50), nullable=False)  # 'domicile', 'loisir' or 'courses'
  address = db.Column(db.String(200), nullable=False)
  transportation_mode = db.Column(
    db.String(50),
    nullable=False)  # 'pied', 'vélo', 'bus', 'Voiture Individuelle', etc.
  average_duration = db.Column(db.Integer, nullable=False)