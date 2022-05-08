from flask import Blueprint, jsonify
from db_direction import get_users, get_user_by_id, get_orders, get_order

pages_blueprint = Blueprint('pages_blueprint', __name__)

@pages_blueprint.route('/users')
def get_all_users():
    return jsonify(get_users())

@pages_blueprint.route('/users/<int:id>')
def get_one_user(id):
    return jsonify(get_user_by_id(id))

@pages_blueprint.route('/orders')
def get_all_orders():
    return jsonify(get_orders())

@pages_blueprint.route('/orders/<int:id>')
def get_one_order(id):
    return jsonify(get_order(id))


