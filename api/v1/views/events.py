#!/usr/bin/python3
"""
This file handles the events url
"""

from models import storage
from models.organization import Organization
from models.event import Event
from models.volunteer import Volunteer
from api.v1.views import app_views
from models.utility import jwt_decode
from flask import jsonify, abort, make_response, request

@app_views.route("/events", methods=["GET"], strict_slashes=False)
def get_events():
    """This will list the available events"""
    events = storage.all(Event).values()
    if events:
        event_list = [value.to_dict() for value in events]
        return jsonify(event_list)
    else:
        return jsonify("Error occured"), 401


@app_views.route("/events", methods=["POST"], strict_slashes=False)
def create_event():
    """This method will handle creating posting"""
    from api.v1.app import app
    token = request.headers.get("Authorization")
    if not token:
        return jsonify("access_token needed"), 401
    org_id = jwt_decode(token, app.config["SECRET_KEY"])
    if not org_id:
        return jsonify("Invalid Token"), 401
    org = storage.get(Organization, org_id)
    if org:
        new_dict = request.get_json()
        new_dict["org_id"] = org.id
        volun_list = new_dict["volunteers"]
        del new_dict["volunteers"]
        events = Event(**new_dict)
        for volunteer in volun_list:
            get_volunteer = storage.filter(Volunteer, "id", volunteer)
            events.volunteers.append(get_volunteer)
        events.save()
        return jsonify({"message": "sucessful creation", "events": events.to_dict()})
    else:
        return abort(404)