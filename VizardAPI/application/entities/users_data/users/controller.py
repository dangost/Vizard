from flask import Blueprint, jsonify, request
from .repository import UsersRepository
from .schema import UserSchema, UserAuntSchema
from application.app import base
import time


users_api = Blueprint('users_controller_api', __name__)

rep = UsersRepository(base)


@users_api.route("/api/Users/" or "/api/Users",
                 methods=['GET'])
def get_all():
    data = rep.get_all()
    return jsonify(UserSchema(many=True).dump(data))


@users_api.route("/api/Users/<int:item_id>/" or "/api/Users/<int:item_id>",
                 methods=['GET'])
def get_id(item_id):
    obj = rep.get_id(item_id)
    if type(obj) is str:
        return obj
    return jsonify(UserSchema(many=False).dump(obj))


@users_api.route("/api/Users/" or "/api/Users",
                 methods=['POST'])
def post():
    json_data = request.get_json()
    obj = UserSchema(many=False).load(json_data)
    result = rep.add(obj)
    return result


@users_api.route("/api/Users/<int:item_id>/" or "/api/Users/<int:item_id>",
                 methods=['PUT'])
def put(item_id):
    json_data = request.get_json()
    obj = UserSchema(many=False).load(json_data)
    result = rep.replace(obj, item_id)
    return result


@users_api.route("/api/Users/<int:item_id>/" or "/api/Users/<int:item_id>",
                 methods=['DELETE'])
def delete(item_id):
    result = rep.remove(item_id)
    return result


@users_api.route("/api/Users/Login/" or "/api/Users/Login", methods=['POST'])
def user_login():
    json_data = request.get_json()
    obj = UserAuntSchema(many=False).load(json_data)
    res = rep.login_check(obj)
    return jsonify(res)



