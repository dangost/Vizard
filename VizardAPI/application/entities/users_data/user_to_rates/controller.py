from flask import Blueprint, jsonify, request
from .repository import UserToRatesRepository
from .schema import UserToRatesSchema
from application.app import base

users_to_rates_api = Blueprint('users_to_rates_controller_api', __name__)

rep = UserToRatesRepository(base)


@users_to_rates_api.route("/api/UserToRates/" or "/api/UserToRates",
                          methods=['GET'])
def get_all():
    data = rep.get_all()
    return jsonify(UserToRatesSchema(many=True).dump(data))


@users_to_rates_api.route("/api/UserToRates/<int:utr_id>/" or "/api/UserToRates/<int:utr_id>",
                          methods=['GET'])
def get_id(utr_id):
    obj = rep.get_id(utr_id)
    if type(obj) is str:
        return obj
    return jsonify(UserToRatesSchema(many=False).dump(obj))


@users_to_rates_api.route("/api/UserToRates/" or "/api/UserToRates",
                          methods=['POST'])
def post():
    json_data = request.get_json()
    result = rep.add(json_data)
    return result


@users_to_rates_api.route("/api/UserToRates/<int:utr_id>/" or "/api/UserToRates/<int:utr_id>",
                          methods=['PUT'])
def put(utr_id):
    json_data = request.get_json()
    result = rep.replace(utr_id, json_data)
    return result


@users_to_rates_api.route("/api/UserToRates/<int:utr_id>/" or "/api/UserToRates/<int:utr_id>",
                          methods=['DELETE'])
def delete(utr_id):
    result = rep.remove(utr_id)
    return result
