from flask import Blueprint, jsonify, request
from .repository import StudiosRepository
from .schema import StudioSchema


studios_controller_api = Blueprint('studios_controller_api', __name__)

rep = StudiosRepository()


@studios_controller_api.route("/api/Studios/" or "/api/Studios", methods=['GET'])
def get_all_studios():
    data = rep.get_all_studios()
    return jsonify(StudioSchema(many=True).dump(data))


@studios_controller_api.route("/api/Studios/<int:studio_id>/" or "/api/Studios/<int:studio_id>", methods=['GET'])
def get_studio_id(studio_id):
    obj = rep.get_id_studio(studio_id)
    if type(obj) is str:
        return obj
    return jsonify(StudioSchema(many=False).dump(obj))


@studios_controller_api.route("/api/Studios/" or "/api/Studios", methods=['POST'])
def post_studio():
    json_data = request.get_json()
    result = rep.post_studio(json_data)
    return result


@studios_controller_api.route("/api/Studios/<int:studio_id>/" or "/api/Studios/<int:studio_id>", methods=['PUT'])
def put_studio(studio_id):
    json_data = request.get_json()
    result = rep.put_studio(studio_id, json_data)
    return result


@studios_controller_api.route("/api/Studios/<int:studio_id>/" or "/api/Studios/<int:studio_id>", methods=['DELETE'])
def delete_studio(studio_id):
    result = rep.delete_studio(studio_id)
    return result


