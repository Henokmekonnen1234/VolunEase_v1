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
        sorted_events = sorted(events, key=lambda x: x.start_time, reverse=True)
        event_list = [value.to_dict() for value in sorted_events]
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
        new_dict["created_date"] = "2023-10-28T10:00:00.000"
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
    
@app_views.route("/events/<id>", methods=["PUT"], strict_slashes=False)
def update_event(id=None):
    """This method will update the volunteer data"""
    from api.v1.app import app
    token = request.headers.get("Authorization")
    if not token:
        return make_response(jsonify({"message": "token not found"}), 401)
    if not id:
        return jsonify("value is not found"), 401
    else:
        org_id = jwt_decode(token, app.config["SECRET_KEY"])
        if org_id is None:
             return jsonify("Invalid Token, please log in again"), 401
        new_dict = request.get_json()
        new_dict["org_id"] = org_id
        volun_list = new_dict["volunteers"]
        del new_dict["volunteers"]
        event = storage.get(Event, id)
        if volun_list:
            for volunteer in volun_list:
                event.volunteers.append(storage.filter(Volunteer, "id", volunteer))
        if event:
            for key, value in new_dict.items():
                if value != None:
                    if key != "id" or key != "update_date" or\
                        key != "created_date":
                        setattr(event, key, value)
            event.save()
            print(event.to_dict())
        else:
            return jsonify("event not found")
        return jsonify("Error unkown")
    
@app_views.route('/events/<id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_event(id=None):
    """
    Deletes a Review Object
    """
    from api.v1.app import app
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Missing token'}), 401
    if not id:
        return jsonify("Value not found")
    org_id = jwt_decode(token, app.config["SECRET_KEY"])
    event = storage.get(Event, id)
    if org_id and event:
        storage.delete(event)
        storage.save()
        return make_response(jsonify({"id": id}), 200)
    else:
        return jsonify("Log in again please")