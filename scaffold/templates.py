# -*- coding: utf-8 -*-
__author__ = 'DeonHeyns'

INIT = """
# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module

# Register blueprint(s)
app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
"""

CONFIG = """
# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
"""

FILES = """
$project$/app/__init__.py
$project$/app/run.py
$project$/app/config.py
$project$/app/module_one/__init__.py
$project$/app/module_one/controllers.py
$project$/app/module_one/models.py
$project$/app/templates/module_one/index.html
$project$/app/static/css/site.css
$project$/app/static/js/script.js
"""

RUN = """
# Run a test server.
from app import app
app.run(host='0.0.0.0', port=8080, debug=True)
"""

STRUCTURE = """
$project$
$project$/env
$project$/app
$project$/app/module_one
$project$/app/templates
$project$/app/templates/module_one
$project$/app/static
$project$/app/static/css
$project$/app/static/js
$project$/app/static/img
"""