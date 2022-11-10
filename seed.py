from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from datetime import date
import csv

import config
from model import db, User, Location, Reading

def load_users():
    print("loading sample users...")

    with open("./data/users.csv") as users_csv:
        users = csv.reader(users_csv, delimiter=",")
        for user in users:

            new_user = User(name=user[0],
                password=user[1],
                email=user[2],
                phone=user[3])

            db.session.add(new_user)
            print("added user {}".format(user[0]))

    db.session.commit()

def load_locations():
    print("loading sample locations...")

    with open("./data/locations.csv") as locations_csv:
        locations = csv.reader(locations_csv, delimiter=",")
        for location in locations:

            location = Location(user=location[0],
                name=location[1],
                lat=location[2],
                lon=location[3],
                upper=location[4],
                lower=location[5])

            db.session.add(location)
            print("added location {}".format(location[1]))

    db.session.commit()

def load_readings():
    print("loading sample readings...")

    with open("./data/readings.csv") as readings_csv:
        readings = csv.reader(readings_csv, delimiter=",")
        for reading in readings:

            reading = Reading(location=reading[0],
                time=date.today(),
                aqi=reading[1])

            db.session.add(reading)
            print("added reading {}".format(reading))

    db.session.commit()


if __name__ == "__main__":
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI

    db.init_app(app)
    with app.app_context():
        load_users()
        load_locations()
        load_readings()