from flask import Blueprint, request, jsonify, redirect, url_for

from ..controller import users_controller
from ..models.models import User

api_scope = Blueprint("api_scope", __name__)

@api_scope.route("/users/<id_>", methods=['GET'])
def get_details(id_):
    user = User(id=id_)
    user_setter = users_controller.details(user)
    return jsonify(user_setter._asdict())