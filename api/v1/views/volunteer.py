#!/usr/bin/python3
""" objects that handle all default RestFul API actions for
Volunteer"""
from models.volunteer import Volunteer
from models.organization import Organization
from models.event import Event
from models import storage
from models.utility import check_token, save_file, delete_file
from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
import os

@app_views.route("/volunteers", methods=["GET"], strict_slashes=False)
def get_volunteers():
    """This method gets all volunteer objects"""
    try:
        token = check_token(request.headers.get('Authorization'))
        if not token:
            return jsonify({'error': 'Log in again'}), 401
        org = storage.get(Organization, token)
        search_q = request.args.get('search', '')
        print(search_q)
        if search_q:
                volunteer = storage.search(Volunteer, search_q, "name")
        else:
            volunteer = storage.all(Volunteer).values()
        list_vol = []
        if org and volunteer:
            for vol in volunteer:
                if org.id == vol.org_id:
                    list_vol.append(vol.to_dict())
        return jsonify(list_vol)
    except Exception as e:
        abort(404)


@app_views.route("/volunteers", methods=["POST"], strict_slashes=False)
def register_volunteer():
    """This method will register the volunteer data"""
    try:
        token = check_token(request.headers.get('Authorization'))
        if not token:
            return jsonify({'error': 'Log in again'}), 401
        org = storage.get(Organization, token)
        if org:
            new_data = request.form.to_dict()
            if 'image' in request.files:
                new_data['image'] = save_file(request.files['image'])
            new_data["org_id"] = org.id
            instance = Volunteer(**new_data)
            instance.save()
            if instance:
                return make_response(jsonify(instance.to_dict()))
            else:
                abort(404)
        else:
            abort(404)
    except Exception as e:
        abort(404)


@app_views.route("/volunteers/<id>", methods=["GET"], strict_slashes=False)
def get_volunteer(id):
    """This method will handle individual value of volunteer"""
    try:
        token = check_token(request.headers.get('Authorization'))
        if not token:
            return jsonify({'error': 'Log in again'}), 401
        org = storage.get(Organization, token)
        if not id:
            return jsonify("value is not found"), 401
        else:
            events = storage.all(Event).values()
            volunteer =  storage.get(Volunteer,  id)
            sum = 0
            event_list = []
            if org and volunteer:
                if volunteer.org_id == org.id:
                    for values  in events:
                        for value in values.volunteers:
                            if volunteer.id == value.id:
                                event_list.append(values.to_dict())
                                sum += values.part_time
                    for value in event_list:
                        if value.get("volunteers"):
                            del value["volunteers"]
                    return jsonify({"volunteer": volunteer.to_dict(),
                                    "part_time": sum,
                                    "event_list": event_list})
                else:
                    abort(404)
            else:
                abort(404)
    except Exception as e:
        abort(404)


@app_views.route("/volunteers/<id>", methods=["DELETE"], strict_slashes=False)
def delete_volunteer(id):
    """This method will delete volunteer data using the id"""
    try:
        token = check_token(request.headers.get('Authorization'))
        if not token:
            return jsonify({'error': 'Log in again'}), 401
        org = storage.get(Organization, token)
        if not id:
            return jsonify("value is not found"), 401
        else:
            volunteer =  storage.get(Volunteer, id)
            if org.id == volunteer.org_id:
                image_file = os.path.basename(volunteer.image)
                if image_file:
                    delete_file(image_file)
                storage.delete(volunteer)
                storage.save()
                return jsonify("successfuly deleted")
            else:
                abort(404)
    except Exception as e:
        abort(404)


@app_views.route("/volunteers/<id>", methods=["PUT"], strict_slashes=False)
def update_volunteer(id=None):
    """This method will update the volunteer data"""
    try:
        token = check_token(request.headers.get('Authorization'))
        if not token:
            return jsonify({'error': 'Log in again'}), 401
        org = storage.get(Organization, token)
        if not id and not org:
            abort(404)
        else:
            new_dict = request.form.to_dict()
            if 'image' in request.files and request.files['image']:
                new_dict['image'] = save_file(request.files['image'])
            volunteer = storage.get(Volunteer, id)
            if not volunteer:
                abort(404)
            for key, value in new_dict.items():
                if value != None:
                    if key != "id" or key != "update_date" or\
                                        key != "created_date":
                        setattr(volunteer, key, value)
            volunteer.save()
            return jsonify(volunteer.to_dict())
    except Exception as e:
        abort(404)