from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
import scraper as sc
import risk as ri
import time 
# https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/
# npm run serve (in client folder)
# source vue_env/bin/activate
# python3 app.py (in dashboard folder)

# configuration
# DEBUG = True

# instantiate the app
app = Flask(__name__)
# app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

global last_updated_risk, risk_data_obj, one_day
global last_updated_macro, macro_data_obj

last_updated_macro = 0
last_updated_risk = 0
one_day = 24 * 60 * 60  
macro_data_obj = None
risk_data_obj = None


# TODO Re-enable in production
@app.route("/", methods=['GET'])
def index():
    print("Serving index page...")
    # return "Hello World"
    return app.send_static_file("index.html")

@app.route('/chart_data', methods=['GET'])
def chart_data():
    print("Serving chart data...")
    global last_updated_macro, macro_data_obj, one_day
    print("Fetching chart data", time.time(), last_updated_macro, time.time() - last_updated_macro)
    if time.time() - last_updated_macro > one_day: 
        print("Updating Macro Data")
        macro_data_obj = sc.scrape_data()
        last_updated_macro = time.time() 

    return jsonify(macro_data_obj)

@app.route('/risk_data', methods=['GET'])
def risk_data():
    print("Serving risk data...")
    global last_updated_risk, risk_data_obj, one_day

    if time.time() - last_updated_risk > one_day: 
        print("Updating Risk Data")
        risk_data_obj = ri.get_risk_report()
        last_updated_risk = time.time() 

    return jsonify(risk_data_obj)

if __name__ == "__main__":
    print("Starting app...")
    app.run()

#https://vishnut.me/blog/ec2-flask-apache-setup.html