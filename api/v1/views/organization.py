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
    if new_dict.get("email"):
        org = storage.filter(Organization, "email", new_dict["email"])
        if org:
            if decrypt(new_dict["password"], org.password):
                token = jwt_encode(org.id, app.config["SECRET_KEY"])
                return jsonify({"message": "successfull", "orgs": org.to_dict()}, token)
            else:
                return abort(404)
        else:
            abort(404)

@app_views.route('/organizations/<id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_organization(id):
    """
    Deletes a Review Object
    """

    org = storage.get(Organization, id)

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

    try:
        org_id = jwt_decode(token, app.config["SECRET_KEY"])
        org = storage.get(Organization, org_id)
        event = [value.to_dict() for value in storage.all(Event).values()]
        volunteer = [value.to_dict() for value in storage.all(Volunteer).values()]
        if org:
            return jsonify({"org": org.to_dict(), "event": event,
                            "volunteer": volunteer})
        else:
            return jsonify({'message': 'Invalid user'}), 401
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401
