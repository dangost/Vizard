from flask import Blueprint
from .model import Studio
from.schema import StudiosSchema

studios_controller_api = Blueprint('studios_controller_api', __name__)


@studios_controller_api.route("/api/Studios/", methods=['GET'])
def test():
    return "studio"


@studios_controller_api.route("/api/Studios/<int:std_id>", methods=['GET'])
def test_id(std_id):
    return "studio " + std_id


