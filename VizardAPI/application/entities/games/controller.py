from flask import Blueprint, request, jsonify
from .schema import GameSchema
from .repository import GamesRepository
from application.app import base
from application.entities.abstract.base_repository import BaseRepository
import time

rep: BaseRepository = GamesRepository(base)

games_controller_api = Blueprint('games_controller_api', __name__)


@games_controller_api.route("/api/Games/" or "/api/Games", methods=['GET'])
def get_all_games():
    data = rep.get_all()
    return jsonify(GameSchema(many=True).dump(data))


@games_controller_api.route("/api/Games/<int:game_id>/" or "/api/Games/<int:game_id>", methods=['GET'])
def get_game_id(game_id):
    obj = rep.get_id(game_id)
    if type(obj) is str:
        return obj
    return jsonify(GameSchema(many=False).dump(obj))


@games_controller_api.route("/api/Games/" or "/api/Games", methods=['POST'])
def post_game():
    json_data = request.get_json()
    game = GameSchema(many=False).load(json_data)
    result = rep.add(game)
    return result


@games_controller_api.route("/api/Games/<int:game_id>/" or "/api/Games/<int:game_id>", methods=['PUT'])
def put_game(game_id):
    json_data = request.get_json()
    game = GameSchema(many=False).load(json_data)
    result = rep.replace(game, game_id)
    return result


@games_controller_api.route("/api/Games/<int:game_id>/" or "/api/Games/<int:game_id>", methods=['DELETE'])
def delete_game(game_id):
    result = rep.remove(game_id)
    return result


@games_controller_api.route("/ip/", methods=['GET'])
def ip():
    return jsonify({'ip': request.remote_addr}), 200
