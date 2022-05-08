from flask import Blueprint, jsonify
from db_direction import get_users, get_user_by_id, get_orders, get_order, get_offer, get_offers

pages_blueprint = Blueprint('pages_blueprint', __name__)

@pages_blueprint.route('/users')
def get_all_users():
    return jsonify(get_users())
                                                    # шаг 3
@pages_blueprint.route('/users/<int:id>')
def get_one_user(id):
    return jsonify(get_user_by_id(id))

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


