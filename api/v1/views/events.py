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
from flask import jsonify, abort, make_response

app_views.route("/events", methods=["GET"], strict_slashes=False)
def get_events():
    """This will list the available events"""
    event = storage.all(Event).values()
    if event:
        event_list = [value.to_dict() for value in event]
        return jsonify(event_list)
    else:
        return jsonify("Error occured"), 401