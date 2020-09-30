from flask import Blueprint
from .model import Genre
from.schema import GenresSchema

genres_controller_api = Blueprint('genres_controller_api', __name__)


@genres_controller_api.route("/api/Genres/", methods=['GET'])
def test():
    return "genre"


@genres_controller_api.route("/api/Genres/<int:genre_id>", methods=['GET'])
def test_id(genre_id):
    return "genre " + genre_id
