#!/usr/bin/python3
""" objects that handle all default RestFul API actions for
Volunteer"""
from models.volunteer import Volunteer
from models.organization import Organization
from models import storage
from models.utility import taken_value
from models.utility import jwt_decode
from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
import logging

@app_views.route("/volunteers", methods=["GET"], strict_slashes=False)
def get_volunteers():
    """This method gets all volunteer objects"""
    from api.v1.app import app
    token = request.headers.get("Authorization")
    if not token:
        return make_response(jsonify({"message": "token not found"}), 401)
    org_id = jwt_decode(token, app.config["SECRET_KEY"])
    if org_id is None:
        return jsonify("Invalid Token, please log in again"), 401
    org = storage.get(Organization, org_id)
    volunteer = storage.all(Volunteer).values()
    list_vol = []
    if org and volunteer:
        for vol in volunteer:
            if org.id == vol.org_id:
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
    if org_id is None:
        return jsonify("Invalid Token, please log in again"), 401
    org = storage.get(Organization, org_id)
    if org:
        new_data = request.get_json()
        new_data["org_id"] = org.id
        present = taken_value(Volunteer, **new_data)
        if present:
            return jsonify(present), 401
        instance = Volunteer(**new_data)
        instance.save()
        if instance:
            return make_response(jsonify(instance.to_dict()))
        else:
            abort(404)
    else:
        abort(404)


@app_views.route("/volunteers/<id>", methods=["GET"], strict_slashes=False)
def get_volunteer(id=None):
    """This method will handle individual value of volunteer"""
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
        org = storage.get(Organization, org_id)
        volunteer =  storage.get(Volunteer, id)
        if org and volunteer:
            if volunteer.org_id == org.id:
                logging.info(volunteer)
                return jsonify(volunteer.to_dict())
            else:
                 return jsonify("Error occured"), 401


@app_views.route("/volunteers/<id>", methods=["DELETE"], strict_slashes=False)
def delete_volunteer(id):
    """This method will delete volunteer data using the id"""
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
        org = storage.get(Organization, org_id)
        volunteer =  storage.get(Volunteer, id)
        if org.id == volunteer.org_id:
            storage.delete(volunteer)
            storage.save()
            return jsonify("successfuly deleted", id)
        else:
            abort(404)