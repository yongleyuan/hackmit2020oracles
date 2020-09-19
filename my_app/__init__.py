import os
from flask import Flask, session, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#load main config
<<<<<<< HEAD
app.config.from_pyfile('../config.py') 
=======
app.config.from_pyfile('../config.py')
>>>>>>> 62f11bbdd51172bb2d74fcc5cb3a7773c399fe1c
db = SQLAlchemy(app)


import my_app.views
<<<<<<< HEAD
import my_app.models
=======
import my_app.models

db.create_all()
>>>>>>> 62f11bbdd51172bb2d74fcc5cb3a7773c399fe1c
