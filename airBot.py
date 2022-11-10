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


with app.app_context():
    db.create_all()

db.session.add(User('admin', 'demo', 'fake@fake.com', '2223334444'))
db.session.commit()

users = User.query.all()
print('created tables and added users')
print(users)

# if __name__ == "__main__":

    # create_database_tables(app)
    # connect_to_db(app)


    # app.run(debug=True)
