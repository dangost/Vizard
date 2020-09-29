from flask import Blueprint
from .model import Studio
from.schema import StudiosSchema

studios_controller_api = Blueprint('studios_controller_api', __name__)


@studios_controller_api.route("/Studios/", methods=['GET'])
def test():
    return "test"


@studios_controller_api.route("/Studios/<int:std_id>", methods=['GET'])
def test(std_id):
    return "test" + std_id


