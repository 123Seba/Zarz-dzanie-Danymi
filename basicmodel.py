from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Correct import statement
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Correct configuration key

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'  # Typo correction: '__tablename__'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    semester = db.Column(db.Integer)

    def __init__(self, name, semester):
        self.name = name
        self.semester = semester

    def __repr__(self):  # Correct indentation
        return f'Student({self.name}, {self.semester})'  # Corrected representation

if __name__ == '__main__':
    app.run(debug=True)


