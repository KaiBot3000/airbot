"""Models and database functions for Airbot"""

from flask_sqlalchemy import SQLAlchemy
import config

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
db = SQLAlchemy()

class User(db.Model):
    """Airbot users"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    user_password = db.Column(db.String, nullable=False)
    user_email = db.Column(db.String(40), nullable=False)
    user_phone = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """What to show when user object printed"""

        return "<User id:%s, username: %s>" % (self.user_id, self.user_name)


class Location(db.Model):
    """Airbot user locations"""

    __tablename__ = "locations"

    location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    location_user = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    location_name = db.Column(db.String(20), nullable=False)
    location_lat = db.Column(db.Integer, nullable=False)
    location_lon = db.Column(db.Integer, nullable=False)
    location_upper = db.Column(db.Integer, nullable=False)
    location_lower = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """What to show when location object printed"""

        return "<Location id:%s, name: %s>" % (self.location_id, self.location_name)


class Reading(db.Model):
    """Airbot location readings"""

    __tablename__ = "readings"

    reading_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    reading_location = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    reading_time = db.Column(db.DateTime, nullable=False)
    reading_aqi = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        """What to show when reading object printed"""

        return "<reading id:%s, time: %s, AQI: %s>" % (self.reading_id, self.reading_time, self.reading_aqi)


def connect_to_db(app):
    """Connects the db to flask app"""

    app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URI
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from airBot import app
    connect_to_db(app)
    print("Connected to DB.")
