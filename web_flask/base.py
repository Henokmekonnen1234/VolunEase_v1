#!/usr/bin/python3
""" Starts a Flash Web Application """

from flask import Flask, render_template, request
from models import storage
from models.organization import Organization
from models.event import Event
from models.volunteer import Volunteer
from models.utility import jwt_decode
from uuid import uuid4
from flask_cors import CORS


app = Flask(__name__)
app.config["SECRET_KEY"] = str(uuid4())
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.teardown_appcontext
def teardown(error):
    """This will close the current session"""
    storage.close()


def find_org(token):
    """This method will find the token and return True if it's
    find otherwise False"""
    from api.v1.app import app as api_app
    if not token:
        return False

    org_id = jwt_decode(token, api_app.config["SECRET_KEY"])
    org = storage.get(Organization, org_id)
    if org:
        return True
    else:
        return False

@app.route("/")
@app.route("/index")
def landing_page():
    """This method will fetch the log in page"""
    return render_template("landing_page.html")

@app.route("/log-in")
def login():
    """This method will fetch the log in page"""
    return render_template("log_in.html")


@app.route("/register")
def register():
    """This method will fetch the register page"""
    return render_template("registration.html")


@app.route("/about-us")
def about_us():
    """This method will fetch the register page"""
    return render_template("about_us.html")


@app.route("/dashboard")
def org_dashboard():
    """This method will fetch organization dasboard page"""
    if find_org(request.headers.get('Authorization')):
        return render_template("organization_dashboard.html")
    else:
        return "Not Found"


@app.route("/volunteers-registration")
def volun_registeer():
    """This method will fetch vounteer registeer page"""
    if find_org(request.headers.get('Authorization')):
        return render_template("volunteer_register.html")
    else:
        return "Not Found"

@app.route("/volunteers-list")
def volun_list():
    """This method will fetch vounteer registeer page"""
    if find_org(request.headers.get('Authorization')):
        return render_template("volunteer_list.html")
    else:
        return "Not Found"


@app.route("/volunteers")
def volun_detail():
    """This method will fetch vounteer registeer page"""
    if find_org(request.headers.get('Authorization')):
        return render_template("volunteer_detail.html")
    else:
        return "Not Found"


@app.route("/create-event")
def event_create():
    """This method will fetch event create page"""
    if find_org(request.headers.get('Authorization')):
        return render_template("create_event.html")
    else:
        return "Not Found"


@app.route("/event-list")
def event_list():
    """This method will fetch event list page"""
    return render_template("event_list.html")


@app.route("/events")
def event_detail():
    """This method will fetch event list page"""
    return render_template("event_detail.html")


if __name__ == "__main__":
    app.run(debug=True)
