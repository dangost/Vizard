from flask import Blueprint, jsonify, request
from .repository import UserToGamesRepository
from .schema import UserToGamesSchema
from application.app import base

users_to_games_controller_api = Blueprint('studios_controller_api', __name__)

rep = UserToGamesRepository(base)


@users_to_games_controller_api.route("/api/UsersToGames/" or "/api/UsersToGames", methods=['GET'])
def get_all():
    data = rep.get_all_utd()
    return jsonify(UserToGamesSchema(many=True).dump(data))


@users_to_games_controller_api.route("/api/UsersToGames/<int:utd_id>/" or "/api/UsersToGames/<int:utd_id>", methods=['GET'])
def get_id(studio_id):
    obj = rep.get_id_utd(studio_id)
    if type(obj) is str:
        return obj
    return jsonify(UserToGamesSchema(many=False).dump(obj))


@users_to_games_controller_api.route("/api/UsersToGames/" or "/api/UsersToGames", methods=['POST'])
def post():
    json_data = request.get_json()
    result = rep.post_utd(json_data)
    return result


@users_to_games_controller_api.route("/api/UsersToGames/<int:utd_id>/" or "/api/UsersToGames/<int:utd_id>",
                                     methods=['PUT'])
def put(utd_id):
    json_data = request.get_json()
    result = rep.put_utd(utd_id, json_data)
    return result


@users_to_games_controller_api.route("/api/UsersToGames/<int:utd_id>/" or "/api/UsersToGames/<int:utd_id>",
                                     methods=['DELETE'])
def delete(utd_id):
    result = rep.delete_utd(utd_id)
    return result
