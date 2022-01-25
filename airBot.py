from flask import Flask
import requests
import json

import config


app = Flask(__name__)

purpleair_base_url = "https://www.purpleair.com/json"
headers = {"X-API-Key": config.api_key}

@app.route("/")
def hey():
    return "<p> Hey there! </p>"

@app.route("/aqi/<int:sensor_id>")
def show_sensor_aqi():
    return "aqi goes here"

def get_sensor_data(sensor_id):
    # hit purple endpoint
    r = requests.get(purpleair_base_url+'?show='+sensor_id, headers)
    # error handling, check for 200
    # parse out value
    raw_sensor_data = r.json()['results'][0]
    parsed_sensor_data = {"label": raw_sensor_data['Label'],
        "aqi": raw_sensor_data['PM2_5Value'],
        }
    # return value
    return parsed_sensor_data
    