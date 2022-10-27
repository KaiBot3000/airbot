"""Utility file to seed database with filtered and processed FUF data"""
from model import User, Location, Reading, connect_to_db, db
from server import app

def load_users():
    """Loads sample users into User table"""
    print("loading sample users...")

    f = open("users.csv")

    line_list = list(f)[0].split()
    for line in line_list:

        new_user = User(user_name=line[0],
            user_password=line[1],
            user_email=line[2],
            user_phone=line[3])

        db.session.add(new_user)

        print("added user {}".format(line[0]))

    db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)

    load_users()
    # load_locations()
    # load_readings()