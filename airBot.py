from flask import Flask
import requests
import json

import config
import dummyDB

app = Flask(__name__)

base_url = 'http://api.openweathermap.org/data/2.5/air_pollution'
api_key = config.api_key

@app.route("/")
def hey():
    return "<p> Hey there! </p>"

@app.route("/status/")
def get_location_status():
    lat = dummyDB.lat
    lon = dummyDB.lon
    # response = requests.get(base_url+'?lat='+lat+'&lon='+lon'&appid='+api_key)
    response = requests.get('http://echo.jsontest.com/key/value/one/two')
    return response.json()

