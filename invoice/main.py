import os
from datetime import date
from dateutil.relativedelta import relativedelta
from flask import Flask, jsonify

app = Flask(__name__)

TAX_RATE = 0.0825
VERSION = os.getenv("APP_VERSION", "dev")


@app.route("/")
def home():
    return "Invoice service running"


@app.route("/version")
def version():
    return jsonify(version=VERSION)


@app.route("/invoice/<amount>")
def invoice(amount):
    try:
        value = float(amount)
    except ValueError:
        return jsonify(error="Invalid amount"), 400
    if value <= 0:
        return jsonify(error="Amount must be positive"), 400
    tax = round(value * TAX_RATE, 2)
    return jsonify(
        subtotal=value,
        tax=tax,
        total=round(value + tax, 2),
        due=str(date.today() + relativedelta(days=30)),
    )