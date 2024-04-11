from flask import Flask, request

from db.connection import get_connection

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/rates", methods=["GET"])
def get_rates():
    conn = get_connection()
    return str(request.args.to_dict())
