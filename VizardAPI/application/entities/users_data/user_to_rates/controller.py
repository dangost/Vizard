from flask import Blueprint, jsonify, request
from .repository import UserToRatesRepository
from .schema import UserToRatesSchema
from application.entities.games.schema import GameSchema
from application.app import base

users_to_games_controller_api = Blueprint('studios_controller_api', __name__)

rep = UserToRatesRepository(base)


@users_to_games_controller_api.route("/api/UserToRates/" or "/api/UserToRates", methods=['GET'])
def get_all():
    data = rep.get_all_utr()
    return jsonify(UserToRatesSchema(many=True).dump(data))


@users_to_games_controller_api.route("/api/UserToRates/<int:utr_id>/" or "/api/UserToRates/<int:utr_id>", methods=['GET'])
def get_id(utr_id):
    obj = rep.get_id_utr(utr_id)
    if type(obj) is str:
        return obj
    return jsonify(UserToRatesSchema(many=False).dump(obj))


@users_to_games_controller_api.route("/api/UserToRates/UserGames/<int:user_id>/" or
                                     "/api/UserToRates/UserGames/<int:user_id>", methods=['GET'])
def get_user_id(user_id):
    collection: list = rep.get_user_games(user_id)
    if len(collection) == 0:
        return []
    return jsonify(GameSchema(many=True).dump(collection))


@users_to_games_controller_api.route("/api/UserToRates/" or "/api/UserToRates", methods=['POST'])
def post():
    json_data = request.get_json()
    result = rep.post_utr(json_data)
    return result


@users_to_games_controller_api.route("/api/UserToRates/<int:utr_id>/" or "/api/UserToRates/<int:utr_id>",
                                     methods=['PUT'])
def put(utr_id):
    json_data = request.get_json()
    result = rep.put_utr(utr_id, json_data)
    return result


@users_to_games_controller_api.route("/api/UserToRates/<int:utr_id>/" or "/api/UserToRates/<int:utr_id>",
                                     methods=['DELETE'])
def delete(utr_id):
    result = rep.delete_utr(utr_id)
    return result
