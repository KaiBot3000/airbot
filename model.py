"""Models and database functions for Airbot"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """Airbot users"""

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)

    def __repr__(self):
        """What to show when user object printed"""

        return "<User id:%s, username: %s>" % (self.id, self.name)

    def __init__(self, name, password, email, phone):
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone


class Location(db.Model):
    """Airbot user locations"""

    __tablename__ = "locations"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    upper = db.Column(db.Integer, nullable=False)
    lower = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """What to show when location object printed"""

        return "<Location id:%s, name: %s>" % (self.id, self.name)


class Reading(db.Model):
    """Airbot location readings"""

    __tablename__ = "readings"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    location = db.Column(db.Integer, db.ForeignKey('locations.id'))
    created_at = db.Column(db.DateTime, default=datetime.now)
    # time = db.Column(db.TIMESTAMP, nullable=False)
    aqi = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        """What to show when reading object printed"""

        return "<reading id:%s, time: %s, AQI: %s>" % (self.id, self.time, self.aqi)
