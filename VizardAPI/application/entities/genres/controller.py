from flask import Blueprint, jsonify, request
from .repository import GenresRepository
from .schema import GenresSchema
from application.app import base
from application.entities.abstract.base_repository import BaseRepository
from ..games.schema import GameSchema
import time

genres_controller_api = Blueprint('genres_controller_api', __name__)

rep: BaseRepository = GenresRepository(base)


@genres_controller_api.route("/api/Genres/" or "/api/Genres", methods=['GET'])
def get_all_genres():
    data = rep.get_all()
    time.sleep(0.1)
    return jsonify(GenresSchema(many=True).dump(data))


@genres_controller_api.route("/api/Genres/<int:genre_id>/" or "/api/Genres/<int:genre_id>", methods=['GET'])
def get_genre_id(genre_id):
    obj = rep.get_id(genre_id)
    if type(obj) is str:
        return obj
    return jsonify(GenresSchema(many=False).dump(obj))


@genres_controller_api.route("/api/Genres/GenreGames/<int:genre_id>/")
def get_genre_games(genre_id):
    games = []
    for game in base.games:
        if game.genre_id == genre_id:
            games.append(game)
    return jsonify(GameSchema(many=True).dump(games))


@genres_controller_api.route("/api/Genres/" or "/api/Genres", methods=['POST'])
def post_genre():
    json_data = request.get_json()
    genre = GenresSchema(many=False).load(json_data)
    result = rep.add(genre)
    return result


@genres_controller_api.route("/api/Genres/<int:genre_id>/" or "/api/Genres/<int:genre_id>", methods=['PUT'])
def put_genre(genre_id):
    json_data = request.get_json()
    genre = GenresSchema(many=False).load(json_data)
    result = rep.replace(genre, genre_id)
    return result


@genres_controller_api.route("/api/Genres/<int:genre_id>/" or "/api/Genres/<int:genre_id>", methods=['DELETE'])
def delete_genre(genre_id):
    result = rep.remove(genre_id)
    return result
