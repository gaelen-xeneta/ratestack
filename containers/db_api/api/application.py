# external dependency imports
from flask import Flask, request

# local imports
from api.db.connection import get_connection

# Initialize a Flask application instance and add a database connection
APP = Flask(__name__)
APP.db_conn = get_connection()
