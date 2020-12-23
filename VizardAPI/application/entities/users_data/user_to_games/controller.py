from flask import Blueprint, jsonify, request
from .repository import UserToGamesRepository
from .schema import UserToGamesSchema
from application.app import base
from application.entities.games.schema import GameSchema
import time


users_to_games_api = Blueprint('users_to_games_controller_api', __name__)

rep = UserToGamesRepository(base)


@users_to_games_api.route("/api/UsersToGames/" or "/api/UsersToGames",
                          methods=['GET'])
def get_all():
    data = rep.get_all()
    return jsonify(UserToGamesSchema(many=True).dump(data))


@users_to_games_api.route("/api/UsersToGames/<int:item_id>/" or "/api/UsersToGames/<int:item_id>",
                          methods=['GET'])
def get_id(item_id):
    obj = rep.get_id(item_id)
    if type(obj) is str:
        return obj
    return jsonify(UserToGamesSchema(many=False).dump(obj))


@users_to_games_api.route("/api/UsersToGames/UserGames/<int:user_id>/",
                          methods=['GET'])
def get_user_games(user_id):
    collection: list = rep.get_user_games(user_id)
    if len(collection) == 0:
        return jsonify([])
    return jsonify(GameSchema(many=True).dump(collection))


@users_to_games_api.route("/api/UsersToGames/" or "/api/UsersToGames",
                          methods=['POST'])
def post():
    json_data = request.get_json()
    obj = UserToGamesSchema(many=False).load(json_data)
    result = rep.add(obj)
    return result


@users_to_games_api.route("/api/UsersToGames/<int:item_id>/" or "/api/UsersToGames/<int:item_id>",
                          methods=['PUT'])
def put(item_id):
    json_data = request.get_json()
    obj = UserToGamesSchema(many=True).load(json_data)
    result = rep.replace(obj, item_id)
    return result


@users_to_games_api.route("/api/UsersToGames/<int:item_id>/" or "/api/UsersToGames/<int:item_id>",
                          methods=['DELETE'])
def delete(item_id):
    result = rep.remove(item_id)
    return result



