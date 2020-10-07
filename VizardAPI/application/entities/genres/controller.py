from flask import Blueprint, jsonify, request
from .repository import GenresRepository
from.schema import GenresSchema

genres_controller_api = Blueprint('genres_controller_api', __name__)

rep = GenresRepository()


@genres_controller_api.route("/api/Genres/" or "/api/Genres", methods=['GET'])
def get_all_genres():
    data = rep.get_all_genres()
    return jsonify(GenresSchema(many=True).dump(data))


@genres_controller_api.route("/api/Genres/<int:game_id>/" or "/api/Genres/<int:game_id>", methods=['GET'])
def get_genre_id(game_id):
    obj = rep.get_id_genre(game_id)
    if type(obj) is str:
        return obj
    return jsonify(GenresSchema(many=False).dump(obj))


@genres_controller_api.route("/api/Genres/" or "/api/Genres", methods=['POST'])
def post_genre():
    json_data = request.get_json()
    result = rep.post_genre(json_data)
    return result


@genres_controller_api.route("/api/Genres/<int:genre_id>/" or "/api/Genres/<int:game_id>", methods=['PUT'])
def put_genre(genre_id):
    json_data = request.get_json()
    result = rep.put_genre(genre_id, json_data)
    return result


@genres_controller_api.route("/api/Games/<int:genre_id>/" or "/api/Games/<int:game_id>", methods=['DELETE'])
def delete_genre(genre_id):
    result = rep.delete_genre(genre_id)
    return result
