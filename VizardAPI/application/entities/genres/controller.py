from flask import Blueprint
from .model import Genre
from.schema import GenresSchema

genres_controller_api = Blueprint('genres_controller_api', __name__)


@genres_controller_api.route("/Genres/", methods=['GET'])
def test():
    return "test"


@genres_controller_api.route("/Genres/<int:genre_id>", methods=['GET'])
def test(genre_id):
    return "test" + genre_id
