#!/usr/bin/python3
""" Starts a Flash Web Application """

from flask import Flask, render_template
from models import storage
from web_flask import app_views
from models.organization import Organization
from models.event import Event
from models.volunteer import Volunteer
from uuid import uuid4
from flask_cors import CORS


app = Flask(__name__)
app.config["SECRET_KEY"] = str(uuid4())
app.register_blueprint(app_views)
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.teardown_appcontext
def teardown(error):
    """This will close the current session"""
    storage.close()

@app.route("/", strict_slashes=False)
@app.route("/index", strict_slashes=False)
def home_page():
    """This method will fetch the home page"""
    return render_template("landing_page.html")


@app.route("/register", strict_slashes=False)
def register():
    """This method will fetch the registration page"""
    return render_template("registration.html")

@app.route("/events", strict_slashes=False)
def event_list():
    """This method will fetch the event list page"""
    return render_template("event_list.html")



if __name__ == "__main__":
    app.run(debug=True)
