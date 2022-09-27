"""Models and database functions for Airbot"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Airbot users"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    user_password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        """What to show when user object printed"""

        return "<User id:%s, username: %s>" % (self.user_id, self.username)


def connect_to_db(app):
    """Connects the db to flask app"""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/airbot_db"
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from airbot import app
    connect_to_db(app)
    print("Connected to DB.")
