from flask import Blueprint, request, jsonify
from .model import Game
from .schema import GamesSchema
from .repository import GamesRepository


rep = GamesRepository()

games_controller_api = Blueprint('games_controller_api', __name__)


@games_controller_api.route("/api/Games", methods=['GET'])
def get_all_games():
    data = rep.get_all_games()
    return jsonify(GamesSchema(many=True).dump(data))


@games_controller_api.route("/api/Games/<int:game_id>", methods=['GET'])
def get_game_id(game_id):
    obj = get_game_id(game_id)
    return str(GamesSchema(many=False).dump(obj))


@games_controller_api.route("/api/Games", methods=['POST'])
def post_game():
    json_data = request.get_json()
    return


@games_controller_api.route("/api/Games/<int:game_id>", methods=['PUT'])
def put_game(game_id):
    return


@games_controller_api.route("/api/Games/<int:game_id>", methods=['DELETE'])
def delete_game(game_id):
    return
