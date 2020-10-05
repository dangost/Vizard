from flask import Blueprint, request, jsonify
from .schema import GamesSchema
from .repository import GamesRepository


rep: GamesRepository = GamesRepository()

games_controller_api = Blueprint('games_controller_api', __name__)


@games_controller_api.route("/api/Games/" or "/api/Games", methods=['GET'])
def get_all_games():
    data = rep.get_all_games()
    return jsonify(GamesSchema(many=True).dump(data))


@games_controller_api.route("/api/Games/<int:game_id>/" or "/api/Games/<int:game_id>", methods=['GET'])
def get_game_id(game_id):
    obj = rep.get_id_game(game_id)
    if type(obj) is str:
        return obj
    return jsonify(GamesSchema(many=False).dump(obj))


@games_controller_api.route("/api/Games/" or "/api/Games", methods=['POST'])
def post_game():
    json_data = request.get_json()
    result = rep.post_game(json_data)
    return result


@games_controller_api.route("/api/Games/<int:game_id>/" or "/api/Games/<int:game_id>", methods=['PUT'])
def put_game(game_id):
    json_data = request.get_json()
    result = rep.put_game(game_id, json_data)
    return result


@games_controller_api.route("/api/Games/<int:game_id>/" or "/api/Games/<int:game_id>", methods=['DELETE'])
def delete_game(game_id):
    result = rep.delete_game(game_id)
    return result
