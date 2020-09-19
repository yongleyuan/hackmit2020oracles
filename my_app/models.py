from my_app import db

nextid = 100000

class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    rate = db.Column(db.Integer)
    hours = db.Column(db.Integer) #not sure what type it should be
    courses = db.Column(db.String(1000))
    est = db.Column(db.String(1000))