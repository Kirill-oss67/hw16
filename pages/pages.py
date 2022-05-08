from flask import Blueprint, jsonify, request
from db_direction import get_users, get_user_by_id, get_orders, get_order, get_offer, get_offers, create_user, \
    update_user_by_id, delete_user

pages_blueprint = Blueprint('pages_blueprint', __name__)


@pages_blueprint.route('/users')
def get_all_users():
    return jsonify(get_users())
    # шаг 3


@pages_blueprint.route('/users/<int:id>', methods=["GET","PUT",'DELETE'])
def get_one_user(id):
    if request.method == 'GET' :
        return jsonify(get_user_by_id(id))
    elif request.method == "PUT":
        data = request.json
        return jsonify(update_user_by_id(id,data))
    elif request.method == "DELETE" :
        delete_user(id)
        return "deleted"

@pages_blueprint.route('/orders')
def get_all_orders():
    return jsonify(get_orders())
    # шаг 4


@pages_blueprint.route('/orders/<int:id>')
def get_one_order(id):
    return jsonify(get_order(id))


@pages_blueprint.route('/offers')
def get_all_offers():
    return jsonify(get_offers())
    # шаг 5


@pages_blueprint.route('/offers/<int:id>')
def get_one_offer(id):
    return jsonify(get_offer(id))


@pages_blueprint.route("/users", methods=['POST'])
def create_user_page():
    data = request.json
    print(type(data))
    result = create_user(data)
    return result