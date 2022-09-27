from flask import Flask
import sqlalchemy
import requests
import psycopg2
import json

import config

app = Flask(__name__)

base_url = "http://api.openweathermap.org/data/2.5/air_pollution"
api_key = config.api_key

@app.route("/")
def hey():
    return "<p> Hey there! </p>"

@app.route("/status/")
def get_location_status():
    lat = dummyDB.lat
    lon = dummyDB.lon
    # response = requests.get(base_url+'?lat='+lat+'&lon='+lon+'&appid='+api_key)
    response = {
        coord: {
            lat: 42.1912,
            lon: -123.2684
            },
        list: [
            {
            components: {
                co: 168.56,
                nh3: 1.52,
                no: 0.04,
                no2: 1.91,
                o3: 63.66,
                pm10: 4.7,
                pm2_5: 3.58,
                so2: 0.12
                },
                dt: 1664070992,
                main: {
                aqi: 1
                }
            }
        ]
    }
    # return response.json()
    return response


def update_data():
    # get current status
    # update db
    return 0

def check_aqi():
    # get current aqi from db
    # get current alert stat
    return 0

if __name__ == "__main__":
    app.run(debug=True)