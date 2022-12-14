from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import sqlalchemy
import requests
import psycopg2
import twilio
import json
import os

import config
from model import db, User, Location, Reading

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI

db.init_app(app)

base_url = "http://api.openweathermap.org/data/2.5/air_pollution"
openweather_api_key = config.OPENWEATHER_API_KEY
twilio_sid = config.TWILIO_ACCOUNT_SID
twilio_token = config.TWILIO_AUTH_TOKEN
twilio_phone = config.TWILIO_PHONE
to_phone = config.TO_PHONE


def sendText(content):
    client = Client(twilio_sid, twilio_token)

    # message = client.messages.create(
    #     to=to_phone,
    #     from_=twilio_phone,
    #     body=content)

    # print(message.sid)

    # FOR TESTING ONLY
    print(f"fake sending {content}")

@app.route("/ping", methods=['GET', 'POST'])
def pong():
    return("pong\n")

# receive a message

@app.route("/sms", methods=['GET', 'POST'])
def sort_sms():
    """Parse and route incoming sms."""

    body = request.values.get('Body', None)
    if body == "status":
        reply = getStatus(request)
    else:
        reply = "I don't understand! Try one of these: ['status']"
    resp = MessagingResponse()
    resp.message = reply
    # return str(resp)
    ## FOR TESTING ONLY
    return(reply)

def getStatus(sms):
    # get phone number from sms
    # get location from db
    # get most recent aqi
    # return status
    return("aqi is 10")



# @app.route("/")
# def hey():
#     return "<p> Hey there! </p>"

# @app.route("/status/<name>")
# def get_location_status():
#     """Get the most recent reading for a given location"""

#     # fetch location from db

#     # if none, return helpful error

#     # if yes, get most recent reading

#     # return reading aqi

#     lat = dummyDB.lat
#     lon = dummyDB.lon
#     # response = requests.get(base_url+'?lat='+lat+'&lon='+lon+'&appid='+api_key)
#     response = {
#         coord: {
#             lat: 42.1912,
#             lon: -123.2684
#             },
#         list: [
#             {
#             components: {
#                 co: 168.56,
#                 nh3: 1.52,
#                 no: 0.04,
#                 no2: 1.91,
#                 o3: 63.66,
#                 pm10: 4.7,
#                 pm2_5: 3.58,
#                 so2: 0.12
#                 },
#                 dt: 1664070992,
#                 main: {
#                 aqi: 1
#                 }
#             }
#         ]
#     }
#     # return response.json()
#     return response


# def update_data():
#     # get current status
#     # update db
#     return 0

# def check_aqi():
#     # get current aqi from db
#     # get current alert stat
#     return 0

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
