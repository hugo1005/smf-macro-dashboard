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
# CORS(app, resources={r'/*': {'origins': '*'}})


data = [{"date":"2019-08-09","value":20.6},{"date":"2019-08-13","value":20.6},{"date":"2019-08-14","value":20.6},{"date":"2019-08-22","value":20.6},{"date":"2019-08-27","value":20.6},{"date":"2019-08-28","value":20.6},{"date":"2019-08-29","value":20.6},{"date":"2019-09-02","value":20.6},{"date":"2019-09-03","value":20.6},{"date":"2019-09-04","value":20.6},{"date":"2019-09-06","value":20.6},{"date":"2019-09-09","value":22.1},{"date":"2019-09-11","value":22.1},{"date":"2019-09-12","value":22.1},{"date":"2019-09-19","value":22.1},{"date":"2019-09-20","value":22.1},{"date":"2019-09-23","value":22.1},{"date":"2019-09-24","value":22.1},{"date":"2019-09-25","value":22.1},{"date":"2019-09-26","value":22.1},{"date":"2019-09-27","value":22.1},{"date":"2019-09-30","value":22.1},{"date":"2019-10-01","value":22.1},{"date":"2019-10-04","value":22.1},{"date":"2019-10-09","value":22.1},{"date":"2019-10-10","value":16.9},{"date":"2019-10-11","value":16.9},{"date":"2019-10-23","value":16.9},{"date":"2019-10-24","value":16.9},{"date":"2019-10-29","value":16.9},{"date":"2019-10-30","value":16.9},{"date":"2019-11-01","value":16.9},{"date":"2019-11-04","value":16.9},{"date":"2019-11-05","value":16.9},{"date":"2019-11-06","value":16.9},{"date":"2019-11-08","value":24.9},{"date":"2019-11-13","value":24.9},{"date":"2019-11-14","value":24.9},{"date":"2019-11-21","value":24.9},{"date":"2019-11-22","value":24.9},{"date":"2019-11-26","value":24.9},{"date":"2019-11-27","value":24.9},{"date":"2019-11-28","value":24.9},{"date":"2019-11-29","value":24.9},{"date":"2019-12-02","value":24.9},{"date":"2019-12-04","value":24.9},{"date":"2019-12-05","value":24.9},{"date":"2019-12-06","value":24.9},{"date":"2019-12-09","value":22.9},{"date":"2019-12-10","value":22.9},{"date":"2019-12-11","value":22.9},{"date":"2019-12-12","value":22.9},{"date":"2019-12-16","value":22.9},{"date":"2019-12-19","value":22.9},{"date":"2019-12-20","value":22.9},{"date":"2019-12-31","value":22.9},{"date":"2020-01-02","value":22.9},{"date":"2020-01-03","value":22.9},{"date":"2020-01-07","value":22.9},{"date":"2020-01-08","value":22.9},{"date":"2020-01-09","value":24.1},{"date":"2020-01-10","value":24.1},{"date":"2020-01-14","value":24.1},{"date":"2020-01-16","value":24.1},{"date":"2020-01-23","value":24.1},{"date":"2020-01-24","value":24.1},{"date":"2020-01-28","value":24.1},{"date":"2020-01-30","value":24.1},{"date":"2020-02-03","value":24.1},{"date":"2020-02-05","value":24.1},{"date":"2020-02-07","value":24.8},{"date":"2020-02-12","value":24.8},{"date":"2020-02-13","value":24.8},{"date":"2020-02-14","value":24.8},{"date":"2020-02-20","value":24.8},{"date":"2020-02-21","value":24.8},{"date":"2020-02-25","value":24.8},{"date":"2020-02-27","value":24.8},{"date":"2020-02-28","value":24.8},{"date":"2020-03-02","value":24.8},{"date":"2020-03-06","value":24.8},{"date":"2020-03-09","value":16.8},{"date":"2020-03-11","value":16.8},{"date":"2020-03-13","value":16.8},{"date":"2020-03-19","value":16.8},{"date":"2020-03-23","value":16.8},{"date":"2020-03-24","value":16.8},{"date":"2020-03-26","value":16.8},{"date":"2020-03-30","value":16.8},{"date":"2020-03-31","value":16.8},{"date":"2020-04-01","value":16.8},{"date":"2020-04-02","value":16.8},{"date":"2020-04-03","value":16.8},{"date":"2020-04-07","value":16.8},{"date":"2020-04-08","value":16.8},{"date":"2020-04-09","value":23.7},{"date":"2020-04-10","value":23.7},{"date":"2020-04-16","value":23.7},{"date":"2020-04-22","value":23.7},{"date":"2020-04-23","value":23.7},{"date":"2020-04-28","value":23.7},{"date":"2020-04-29","value":23.7},{"date":"2020-04-30","value":23.7},{"date":"2020-05-01","value":23.7},{"date":"2020-05-04","value":23.7},{"date":"2020-05-05","value":23.7},{"date":"2020-05-08","value":25.6},{"date":"2020-05-12","value":25.6},{"date":"2020-05-14","value":25.6},{"date":"2020-05-15","value":25.6},{"date":"2020-05-20","value":25.6},{"date":"2020-05-21","value":25.6},{"date":"2020-05-25","value":25.6},{"date":"2020-05-26","value":25.6},{"date":"2020-05-28","value":25.6},{"date":"2020-06-01","value":25.6},{"date":"2020-06-03","value":25.6},{"date":"2020-06-04","value":25.6},{"date":"2020-06-05","value":25.6},{"date":"2020-06-09","value":9.1},{"date":"2020-06-10","value":9.1},{"date":"2020-06-16","value":9.1},{"date":"2020-06-17","value":9.1},{"date":"2020-06-19","value":9.1},{"date":"2020-06-22","value":9.1},{"date":"2020-06-23","value":9.1},{"date":"2020-06-25","value":9.1},{"date":"2020-06-29","value":9.1},{"date":"2020-06-30","value":9.1},{"date":"2020-07-01","value":9.1},{"date":"2020-07-02","value":9.1},{"date":"2020-07-08","value":9.1},{"date":"2020-07-09","value":7.0},{"date":"2020-07-14","value":7.0},{"date":"2020-07-15","value":7.0},{"date":"2020-07-23","value":7.0},{"date":"2020-07-24","value":7.0},{"date":"2020-07-28","value":7.0},{"date":"2020-07-30","value":7.0},{"date":"2020-08-03","value":7.0},{"date":"2020-08-05","value":7.0},{"date":"2020-08-07","value":22.4},{"date":"2020-08-12","value":22.4},{"date":"2020-08-13","value":22.4},{"date":"2020-08-21","value":22.4},{"date":"2020-08-25","value":22.4},{"date":"2020-08-27","value":22.4},{"date":"2020-08-28","value":22.4},{"date":"2020-08-31","value":22.4},{"date":"2020-09-01","value":22.4},{"date":"2020-09-03","value":22.4},{"date":"2020-09-04","value":22.4},{"date":"2020-09-08","value":21.0},{"date":"2020-09-09","value":21.0},{"date":"2020-09-11","value":21.0},{"date":"2020-09-18","value":21.0},{"date":"2020-09-22","value":21.0},{"date":"2020-09-23","value":21.0},{"date":"2020-09-29","value":21.0},{"date":"2020-09-30","value":21.0},{"date":"2020-10-01","value":21.0},{"date":"2020-10-02","value":21.0},{"date":"2020-10-06","value":21.0},{"date":"2020-10-07","value":21.0},{"date":"2020-10-08","value":16.5},{"date":"2020-10-13","value":16.5},{"date":"2020-10-22","value":16.5},{"date":"2020-10-23","value":16.5},{"date":"2020-10-27","value":16.5},{"date":"2020-10-28","value":16.5},{"date":"2020-10-29","value":16.5},{"date":"2020-10-30","value":16.5},{"date":"2020-11-02","value":16.5},{"date":"2020-11-04","value":16.5},{"date":"2020-11-06","value":16.5}]

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

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify(data)

@app.route('/chart_test', methods=['GET'])
def chart_test():
    return jsonify(data)

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
        risk_data_obj = ri.get_attribution_report()
        last_updated_risk = time.time() 

    return jsonify(risk_data_obj)

if __name__ == "__main__":
    print("Starting app...")
    app.run()

#https://vishnut.me/blog/ec2-flask-apache-setup.html