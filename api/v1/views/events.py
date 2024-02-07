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
        return jsonify([])


@app_views.route("/events/<id>", methods=["GET"], strict_slashes=False)
def get_event(id=None):
    """This will return event data using the id"""
    if not id:
        return jsonify("value is not provided"), 401
    event = storage.get(Event, id)
    if event:
        volun_list = [value.to_dict() for value in event.volunteers]
        del event.volunteers
        return jsonify({"event": event.to_dict(), "volun_list": volun_list})


@app_views.route("/events", methods=["POST"], strict_slashes=False)
def create_event():
    """This method will handle creating posting"""
    from api.v1.app import app
    token = request.headers.get("Authorization")
    new_dict = request.get_json()
    if not token:
        return jsonify("access_token needed"), 401
    org_id = jwt_decode(token, app.config["SECRET_KEY"])
    if not org_id:
        return jsonify("Invalid Token"), 401
    org = storage.get(Organization, org_id)
    if org:
        new_dict["org_id"] = org.id
        volun_list = new_dict["volunteers"]
        del new_dict["volunteers"]
        events = Event(**new_dict)
        for volunteer in volun_list:
            events.volunteers.append(storage.filter(Volunteer, "id", volunteer))
        part_time = events.end_time - events.start_time
        events.part_time = float(part_time.total_seconds() / 3600.0)
        events.save()
        del events.volunteers
        return jsonify({"message": "sucessful creation",
                        "events": events.to_dict()})
    else:
        return abort(404)
    
