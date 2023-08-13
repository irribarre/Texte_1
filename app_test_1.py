# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Bonjour, hello. Ceci est le fichier run_app_test_1.py ! Endpoint : dashboard, dashboard_1"

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard_1/')
def dashboard_1():
    return render_template('dashboard_1.html')

if __name__ == "__main__":
    app.run(debug=True)
