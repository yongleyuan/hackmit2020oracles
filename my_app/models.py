from my_app import db

class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    rate = db.Column(db.Integer)
    hours = db.Column(db.Integer) #not sure what type it should be
    courses = db.Column(db.String(200))
