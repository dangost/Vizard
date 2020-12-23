from flask import Blueprint, jsonify, request
from .repository import UserToRatesRepository
from .schema import UserToRatesSchema
from application.app import base
import time

users_to_rates_api = Blueprint('users_to_rates_controller_api', __name__)

rep = UserToRatesRepository(base)


@users_to_rates_api.route("/api/UserToRates/" or "/api/UserToRates",
                          methods=['GET'])
def get_all():
    time.sleep(0.1)
    data = rep.get_all()
    time.sleep(0.1)
    return jsonify(UserToRatesSchema(many=True).dump(data))


@users_to_rates_api.route("/api/UserToRates/<int:utr_id>/" or "/api/UserToRates/<int:utr_id>",
                          methods=['GET'])
def get_id(utr_id):
    time.sleep(0.1)
    obj = rep.get_id(utr_id)
    if type(obj) is str:
        return obj
    time.sleep(0.1)
    return jsonify(UserToRatesSchema(many=False).dump(obj))


@users_to_rates_api.route("/api/UserToRates/" or "/api/UserToRates",
                          methods=['POST'])
def post():
    time.sleep(0.1)
    json_data = request.get_json()
    result = rep.add(json_data)
    time.sleep(0.1)
    return result


@users_to_rates_api.route("/api/UserToRates/<int:utr_id>/" or "/api/UserToRates/<int:utr_id>",
                          methods=['PUT'])
def put(utr_id):
    time.sleep(0.1)
    json_data = request.get_json()
    result = rep.replace(utr_id, json_data)
    time.sleep(0.1)
    return result


@users_to_rates_api.route("/api/UserToRates/<int:utr_id>/" or "/api/UserToRates/<int:utr_id>",
                          methods=['DELETE'])
def delete(utr_id):
    time.sleep(0.1)
    result = rep.remove(utr_id)
    time.sleep(0.1)
    return result
