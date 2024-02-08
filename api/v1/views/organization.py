#!/usr/bin/python3
""" objects that handle all default RestFul API actions for
Organization"""

from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
from models.organization import Organization
from models.volunteer import Volunteer
from models.event import Event
from models import storage
from models.utility import encrypt, decrypt, jwt_encode, jwt_decode
from models.utility import taken_value
import jwt

@app_views.route("/organizations", methods=["GET"], strict_slashes=False)
def get_organizations():
    """This method gets all organization objects"""
    organization = storage.all(Organization).values()
    list_org = []
    for orgs in organization:
        list_org.append(orgs.to_dict())
    return jsonify(list_org)

@app_views.route("/organizations", methods=["POST"], strict_slashes=False)
def register_organization():
    """This method will register organization data"""
    new_dict = request.get_json()
    present = taken_value(Organization, **new_dict)
    if present:
        return jsonify(present), 401
    new_dict["password"] = encrypt(new_dict["password"])
    instance = Organization(**new_dict)
    instance.save()
    return jsonify(instance.to_dict())

@app_views.route("/login", methods=["POST"], strict_slashes=False)
def log_in():
    """This method will use to log in to the dashboard"""
    from api.v1.app import app
    new_dict = request.get_json()
    print(new_dict)
    if new_dict.get("email"):
        org = storage.filter(Organization, "email", new_dict["email"])
        if org:
            if decrypt(new_dict["password"], org.password):
                token = jwt_encode(org.id, app.config["SECRET_KEY"])
                response_data = {
                    "message": "successfull",
                    "orgs": org.to_dict(),
                    "token": token
                }
                return make_response(jsonify(response_data), 200)
            else:
                return make_response(jsonify({"error": "Invalid password"}), 401)
        else:
            return make_response(jsonify({"error": "Organization not found"}), 404)
    else:
        return make_response(jsonify({"error": "Invalid request data"}), 400)

@app_views.route('/organizations', methods=['DELETE'],
                 strict_slashes=False)
def delete_organization():
    """
    Deletes a Review Object
    """
    from api.v1.app import app
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Missing token'}), 401
    org_id = jwt_decode(token, app.config["SECRET_KEY"])
    org = storage.get(Organization, org_id)
    if not org:
        abort(404)
    storage.delete(org)
    storage.save()
    return make_response(jsonify({"id": id}), 200)

@app_views.route('/dashboard', methods=["GET"], strict_slashes=False)
def dashboard():
    """This method handeles the request after log_in"""
    from api.v1.app import app
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Missing token'}), 401

    org_id = jwt_decode(token, app.config["SECRET_KEY"])
    org = storage.get(Organization, org_id)
    events = storage.all(Event).values()
    events_year = {}
    volun_year = {}
    year = []
    for value in events:
        if value.created_date.year not in year:
            year.append(value.created_date.year)
    
    if org:
        return jsonify({"org": org.to_dict()})
    else:
        return jsonify({'message': 'Invalid user'}), 401
    

@app_views.route("/organizations", methods=["PUT"], strict_slashes=False)
def update_organization():
    """This method will update the organization"""
    from api.v1.app import app
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Missing token'}), 401
    org_id = jwt_decode(token, app.config["SECRET_KEY"])
    org = storage.get(Organization, org_id)
    if org:
        new_dict =  request.get_json()
        new_dict["password"] = encrypt(new_dict["password"])
        for key, value in new_dict.items():
            if key != "id" or "created_date" != key or\
                 "updated_date" != key:
                setattr(org, key, value)
        org.save()
        response = make_response(jsonify(org.to_dict()))
        response.headers["Authorization"] = token
        return response
    else:
        abort(404)