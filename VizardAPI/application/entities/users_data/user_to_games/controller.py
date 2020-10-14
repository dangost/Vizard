from flask import Blueprint, jsonify, request
from .repository import UserToGamesRepository
from .schema import UserToGamesSchema

studios_controller_api = Blueprint('studios_controller_api', __name__)

rep = UserToGamesRepository()


@studios_controller_api.route("/api/Studios/" or "/api/Studios", methods=['GET'])
def get_all():
    data = rep.get_all_utd()
    return jsonify(UserToGamesRepository(many=True).dump(data))


@studios_controller_api.route("/api/Studios/<int:studio_id>/" or "/api/Studios/<int:studio_id>", methods=['GET'])
def get_id(studio_id):
    obj = rep.get_id_utd(studio_id)
    if type(obj) is str:
        return obj
    return jsonify(UserToGamesRepository(many=False).dump(obj))


@studios_controller_api.route("/api/Studios/" or "/api/Studios", methods=['POST'])
def post():
    json_data = request.get_json()
    result = rep.post_utd(json_data)
    return result


@studios_controller_api.route("/api/Studios/<int:studio_id>/" or "/api/Studios/<int:studio_id>", methods=['PUT'])
def put(studio_id):
    json_data = request.get_json()
    result = rep.put_utd(studio_id, json_data)
    return result


@studios_controller_api.route("/api/Studios/<int:studio_id>/" or "/api/Studios/<int:studio_id>", methods=['DELETE'])
def delete(studio_id):
    result = rep.delete_utd(studio_id)
    return result


