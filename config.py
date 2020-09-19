import os

DEBUG=True

base = os.path.abspath(os.path.dirname(__file__))
<<<<<<< HEAD
# create a file called 'app.db' in your repo that holds the database
# delete this file to clear the database
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base, 'app.db') 
SQLALCHEMY_TRACK_MODIFICATIONS = False
=======
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
>>>>>>> 62f11bbdd51172bb2d74fcc5cb3a7773c399fe1c
