from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import requests
import psycopg2
import json
import os

import config

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI

db = SQLAlchemy(app)

# base_url = "http://api.openweathermap.org/data/2.5/air_pollution"
# api_key = config.API_KEY

# @app.route("/")
# def hey():
#     return "<p> Hey there! </p>"

# @app.route("/status/")
# def get_location_status():
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

# def create_database_tables(app):
#     # check if tables exist

#     # if not, create
#     from model import User, Location, Reading
#     with app.app_context():
#         db.create_all()

#         db.session.add(User('admin', 'demo', 'fake@fake.com', 2223334444))
#         db.session.commit()

#         users = User.query.all()
#         print('created tables and added users')
#         print(users)

# create_database_tables(app)

# from model import User, Location, Reading

# class User(db.Model):
#     """Airbot users"""

#     __tablename__ = "users"

#     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     user_name = db.Column(db.String(20), unique=True, nullable=False)
#     user_password = db.Column(db.String, nullable=False)
#     user_email = db.Column(db.String(40), nullable=False)
#     user_phone = db.Column(db.Integer, nullable=False)

#     def __repr__(self):
#         """What to show when user object printed"""

#         return "<User id:%s, username: %s>" % (self.user_id, self.user_name)

#     def __init__(self, name, password, email, phone):
#         self.user_name = name
#         self.user_password = password
#         self.user_email = email
#         self.user_phone = phone

class User(db.Model):
    __tablename__ = "users"

    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String, nullable=False, unique=True)
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """What to show when user object printed"""

        return "<User id:%s, username: %s>" % (self.user_id, self.user_name)

    def __init__(self, name, password, email, phone):
        self.user_name = name
        self.user_password = password
        self.user_email = email
        self.user_phone = phone

with app.app_context():
    db.create_all()

# db.session.add(User('admin', 'demo', 'fake@fake.com', 2223334444))
# db.session.commit()

# users = User.query.all()
# print('created tables and added users')
# print(users)

# if __name__ == "__main__":

    # create_database_tables(app)
    # connect_to_db(app)


    # app.run(debug=True)
