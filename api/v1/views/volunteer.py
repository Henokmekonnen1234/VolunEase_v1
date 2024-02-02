#!/usr/bin/python3
""" objects that handle all default RestFul API actions for
Volunteer"""
from models.volunteer import Volunteer
from models.organization import Organization
from models import storage
from models.utility import jwt_decode
from api.v1.views import app_views
from flask import jsonify, request, abort, make_response

@app_views.route("/volunteers", methods=["GET"], strict_slashes=False)
def get_volunteers():
    """This method gets all volunteer objects"""
    volunteer = storage.all(Volunteer).values()
    list_vol = []
    for vol in volunteer:
        list_vol.append(vol.to_dict())
    return jsonify(list_vol)

@app_views.route("/volunteers", methods=["POST"], strict_slashes=False)
def register_volunteer():
    """This method will register the volunteer data"""
    from api.v1.app import app
    token = request.headers.get("Authorization")
    if not token:
        return make_response(jsonify({"message": "token not found"}), 401)
    org_id = jwt_decode(token, app.config["SECRET_KEY"])
    org = storage.get(Organization, org_id)
    if org:
        new_data = request.get_json()
        new_data["org_id"] = org.id
        instance = Volunteer(**new_data)
        instance.save()
        if instance:
            return make_response(jsonify(instance.to_dict()))
        else:
            abort(404)
    else:
        abort(404)