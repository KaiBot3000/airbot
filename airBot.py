from flask import Flask
import requests

app = Flask(__name__)

purpleair_url = "https://www.purpleair.com/json"

@app.route("/")
def hey():
    return "<p> Hey there! </p>"

@app.route("/aqi/<int:sensor_id>")
def show_sensor_aqi():
    return "aqi goes here"

def get_aqi_from_sensor(sensor_id):
    return 30
    