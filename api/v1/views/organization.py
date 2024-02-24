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
from models.utility import taken_value, save_file, delete_file
from models.utility import check_token
import os

@app_views.route("/organizations", methods=["GET"], strict_slashes=False)
def get_org():
    """This method gets all organization objects"""
    try:
        token = check_token(request.headers.get('Authorization'))
        if not token:
            return jsonify({'error': 'Log in again'}), 401
        org = storage.get(Organization, token)
        if org:
            return jsonify(org.to_dict())
        else:
            abort(404)
    except Exception as e:
        abort(404)



@app_views.route("/organizations", methods=["POST"], strict_slashes=False)
def register_organization():
    """This method will register organization data"""
    try:
        new_dict = request.form.to_dict()
        present = taken_value(Organization, **new_dict)
        if present:
            return jsonify({"error": present}), 401
        if 'image' in request.files:
                new_dict['image'] = save_file(request.files['image'])
        if 'legal_document' in request.files:
            new_dict['legal_document'] = save_file(request.files['legal_document'])
        new_dict["password"] = encrypt(new_dict["password"])
        instance = Organization(**new_dict)
        instance.save()
        return jsonify(instance.to_dict())
    except Exception as e:
        abort(404)

@app_views.route("/login", methods=["POST"], strict_slashes=False)
def log_in():
    """This method will use to log in to the dashboard"""
    from api.v1.app import app
    try:
        new_dict = request.get_json()
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
                    return jsonify({"error": "Invalid password"}), 401
            else:
                return jsonify({"error": "Email not found"}), 404
        else:
            abort(404)
    except Exception as e:
        abort(404)

@app_views.route('/organizations', methods=['DELETE'],
                 strict_slashes=False)
def delete_organization():
    """
    Deletes a Review Object
    """
    try:
        token = check_token(request.headers.get('Authorization'))
        if not token:
            return jsonify({'error': 'Log in again'}), 401
        org = storage.get(Organization, token)
        if not org:
            abort(404)
        image_file = os.path.basename(org.image)
        doc_file = os.path.basename(org.legal_document)
        if image_file:
            delete_file(image_file)
        if doc_file:
            delete_file(doc_file)
        storage.delete(org)
        storage.save()
        return jsonify("Successfully deleted"), 200
    except Exception as e:
        print(e)
        abort(404)

@app_views.route('/dashboard', methods=["GET"], strict_slashes=False)
def dashboard():
    """This method handeles the request after log_in"""
    try:
        token = check_token(request.headers.get('Authorization'))
        if token:
            org = storage.get(Organization, token)
            events = storage.all(Event).values()
            volunteer = storage.all(Volunteer).values()
            events_year = eachList(org, events)
            volun_year = eachList(org, volunteer)
            if org:
                return jsonify({"org": org.to_dict(),
                                "events_year": events_year,
                                "volun_year": volun_year})
            else:
                abort(404)
        else:
            return jsonify({'error': 'Log in again'}), 401
    except Exception as e:
        abort(404)


@app_views.route("/organizations", methods=["PUT"], strict_slashes=False)
def update_organization():
    """This method will update the organization"""
    try:
        token = check_token(request.headers.get('Authorization'))
        if not token:
            return jsonify({'error': 'Log in again'}), 401
        org = storage.get(Organization, token)
        if org:
            new_dict = request.form.to_dict()
            if 'image' in request.files and request.files['image']:
                new_dict['image'] = save_file(request.files['image'])
            if 'legal_document' in request.files and request.files['legal_document']:
                new_dict['legal_document'] = save_file(request.files['legal_document'])
            if new_dict["password"] != None:
                new_dict["password"] = encrypt(new_dict["password"])
            for key, value in new_dict.items():
                if value != None:
                    if key != "id" or "created_date" != key or\
                                        "updated_date" != key:
                        setattr(org, key, value)
            org.save()
            return jsonify({"e": "Update Successfull"})
        else:
            abort(404)
    except Exception as e:
        abort(404)


def eachList(org, lists):
    """This will return each year counting events or volunteers in
    each year"""
    try:
        year_pair = {}
        for value in lists:
                if org.id == value.org_id:
                    if value.created_date.year not in year_pair.keys():
                        year_pair[value.created_date.year] = 0
        for key, value in year_pair.items():
            count = 0
            for values in lists:
                if key == values.created_date.year and\
                    org.id == values.org_id:
                    count += 1
            year_pair[key] = count
        return year_pair
    except Exception as e:
        abort(404)
