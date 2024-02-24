#!/usr/bin/python3
"""
This file handles the events url
"""

from datetime import datetime
from models import storage
from models.organization import Organization
from models.event import Event
from models.volunteer import Volunteer
from api.v1.views import app_views
from models.utility import jwt_decode, UPLOAD_FOLDER
from flask import jsonify, abort, make_response, request
import os

time = "%Y-%m-%dT%H:%M:%S.%f"


@app_views.route("/events", methods=["GET"], strict_slashes=False)
def get_events():
    """This will list the available events"""
    search_q = request.args.get('search', '')
    print(search_q)
    if search_q:
        events = storage.search(Event, search_q, "title")
    else:
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
    new_dict = request.form.to_dict()
    if 'image' in request.files:
        image_file = request.files['image']
        image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
        image_file.save(image_path)
        new_dict['image'] = f'/uploaded/{image_file.filename}'
    if not token:
        return jsonify("access_token needed"), 401
    org_id = jwt_decode(token, app.config["SECRET_KEY"])
    if not org_id:
        return jsonify("Invalid Token"), 401
    org = storage.get(Organization, org_id)
    if org:
        new_dict["org_id"] = org.id
        if new_dict["volunteers"]:
            volun_list = new_dict["volunteers"].split(",")
            del new_dict["volunteers"]
        if new_dict["start_time"]:
            new_dict["start_time"] = new_dict["start_time"] + ":00.000"
        if new_dict["end_time"]:
            new_dict["end_time"] = new_dict["end_time"] + ":00.000"
        events = Event(**new_dict)
        for volunteer in volun_list:
            events.volunteers.append(storage.filter(Volunteer, "id", volunteer))
        part_time = events.end_time - events.start_time
        events.part_time = float(part_time.total_seconds() / 3600.0)
        events.save()
        del events.volunteers
        return jsonify({"message": "sucessfully created",
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
        new_dict = request.form.to_dict()
        if 'image' in request.files and request.files['image']:
            image_file = request.files['image']
            image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
            image_file.save(image_path)
            new_dict['image'] = f'/uploaded/{image_file.filename}'
        new_dict["org_id"] = org_id
        volun_list = []
        if new_dict["volunteers"]:
            volun_list = new_dict["volunteers"].split(",")
        del new_dict["volunteers"]
        if new_dict["start_time"]:
            new_dict["start_time"] = new_dict["start_time"] + ":00.000"
            start_time = datetime.strptime(new_dict["start_time"], time)
        if new_dict["end_time"]:
            new_dict["end_time"] = new_dict["end_time"] + ":00.000"
            end_time = datetime.strptime(new_dict["end_time"], time)
        event = storage.get(Event, id)
        if volun_list and type(volun_list) == list:
            for volunteer in volun_list:
                event.volunteers.append(storage.filter(Volunteer, "id", volunteer))
        if event:
            for key, value in new_dict.items():
                if value != None:
                    if key != "id" or key != "update_date" or\
                        key != "created_date":
                        print(f"key value {key} {value}")
                        setattr(event, key, value)
            part_time = end_time - start_time
            event.part_time = float(part_time.total_seconds() / 3600.0)
            event.save()
            del event.volunteers
            return jsonify({"message": "Successfully updated",
                            "event": event.to_dict()})
        else:
            return jsonify({"message": "event not found"})


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
    title = event.title
    if org_id and event:
        image_file = os.path.basename(event.image, '')
        if image_file:
            image_path = os.path.join(UPLOAD_FOLDER, image_file)
            if os.path.exists(image_path):
                os.remove(image_path)
        storage.delete(event)
        storage.save()
        return make_response(jsonify({"message": f"{title} successfully deleted"}), 200)
    else:
        return jsonify("Log in again please")