from flask import Blueprint, jsonify, request
from db_direction import get_users, get_user_by_id, get_orders, get_order, get_offer, get_offers, create_user, \
    update_user_by_id, delete_user, create_order, delete_order, delete_offer, create_offer, update_order_by_id, \
    update_offer_by_id

pages_blueprint = Blueprint('pages_blueprint', __name__)


@pages_blueprint.route('/users', methods=['GET', 'POST'])
def get_all_users():
    if request.method == 'GET':
        return jsonify(get_users())  # шаг 3
    elif request.method == 'POST':
        data = request.json
        result = create_user(data)
        return result


@pages_blueprint.route('/users/<int:id>', methods=["GET", "PUT", 'DELETE'])
def get_one_user(id):
    if request.method == 'GET':
        return jsonify(get_user_by_id(id))
    elif request.method == "PUT":
        data = request.json
        return jsonify(update_user_by_id(id, data))
    elif request.method == "DELETE":
        delete_user(id)
        return "deleted"


@pages_blueprint.route('/orders', methods=['GET', 'POST'])
def get_all_orders():
    if request.method == 'GET':
        return jsonify(get_orders())  # шаг 4
    elif request.method == 'POST':      # метод ПОСТ для добавления заказа
        data = request.json
        create_order(data)
        return 'posted'


@pages_blueprint.route('/orders/<int:id>', methods=["GET", "PUT", 'DELETE'])
def get_one_order(id):
    if request.method == 'GET':
        return jsonify(get_order(id))
    elif request.method == "DELETE":
        delete_order(id)
        return 'deleted'
    elif request.method == "PUT":
        data = request.json
        return jsonify(update_order_by_id(id, data))


@pages_blueprint.route('/offers', methods=['GET', 'POST'])
def get_all_offers():
    if request.method == 'GET':
        return jsonify(get_offers())  # шаг 5
    elif request.method == 'POST':
        data = request.json
        create_offer(data)
        return 'posted'


@pages_blueprint.route('/offers/<int:id>', methods=["GET", "PUT", 'DELETE'])
def get_one_offer(id):
    if request.method == 'GET':
        return jsonify(get_offer(id))
    elif request.method == "DELETE":
        delete_offer(id)                # Использование 3 методов ["GET", "PUT", 'DELETE'] для получения, обновления и удаления данных предложения
        return 'deleted'
    elif request.method == "PUT":
        data = request.json
        return jsonify(update_offer_by_id(id, data))
