from flask import Flask, jsonify
import time
import scraper as sc
import risk as ri

app = Flask(__name__)

last_updated_macro = 0
last_updated_risk = 0
one_day = 24 * 60 * 60  
macro_data_obj = None
risk_data_obj = None

if __name__ == "__main__":
 app.run()

@app.route('/')
def hello():
    return app.send_static_file("index.html")

# @app.route('/chart_data', methods=['GET'])
# def chart_data():
#     print("Serving chart data...")
#     global last_updated_macro, macro_data_obj, one_day
#     print("Fetching chart data", time.time(), last_updated_macro, time.time() - last_updated_macro)
#     if time.time() - last_updated_macro > one_day: 
#         print("Updating Macro Data")
#         macro_data_obj = sc.scrape_data()
#         last_updated_macro = time.time() 

#     return jsonify(macro_data_obj)

# @app.route('/risk_data', methods=['GET'])
# def risk_data():
#     print("Serving risk data...")
#     global last_updated_risk, risk_data_obj, one_day

#     if time.time() - last_updated_risk > one_day: 
#         print("Updating Risk Data")
#         risk_data_obj = ri.get_attribution_report()
#         last_updated_risk = time.time() 

#     return jsonify(risk_data_obj)