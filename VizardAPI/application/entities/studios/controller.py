from flask import Blueprint, jsonify, request
from .repository import StudiosRepository
from .schema import StudioSchema
from application.app import base
from application.entities.abstract.base_repository import BaseRepository


studios_controller_api = Blueprint('studios_controller_api', __name__)

rep: BaseRepository = StudiosRepository(base)


@studios_controller_api.route("/api/Studios/" or "/api/Studios", methods=['GET'])
def get_all_studios():
    data = rep.get_all()
    return jsonify(StudioSchema(many=True).dump(data))


@studios_controller_api.route("/api/Studios/<int:studio_id>/" or "/api/Studios/<int:studio_id>", methods=['GET'])
def get_studio_id(studio_id):
    obj = rep.get_id(studio_id)
    if type(obj) is str:
        return obj
    return jsonify(StudioSchema(many=False).dump(obj))


@studios_controller_api.route("/api/Studios/" or "/api/Studios", methods=['POST'])
def post_studio():
    json_data = request.get_json()
    studio = StudioSchema(many=False).load(json_data)
    result = rep.add(studio)
    return result


@studios_controller_api.route("/api/Studios/<int:studio_id>/" or "/api/Studios/<int:studio_id>", methods=['PUT'])
def put_studio(studio_id):
    json_data = request.get_json()
    studio = StudioSchema(many=True).load(json_data)
    result = rep.replace(studio, studio_id)
    return result


@studios_controller_api.route("/api/Studios/<int:studio_id>/" or "/api/Studios/<int:studio_id>", methods=['DELETE'])
def delete_studio(studio_id):
    result = rep.remove(studio_id)
    return result


