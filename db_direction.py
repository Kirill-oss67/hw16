from flask_sqlalchemy import SQLAlchemy
from utils import get_json_data

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    email = db.Column(db.String(50))
    role = db.Column(db.String(50))
    phone = db.Column(db.String(50))


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    order = db.relationship('Order')


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(400))
    start_date = db.Column(db.String(50))
    end_date = db.Column(db.String(50))
    address = db.Column(db.String(150))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', foreign_keys=[customer_id])
    user_1 = db.relationship('User', foreign_keys=[executor_id])


def make_data_users(data_list):
    made_data = []
    for i in data_list:
        user = User(id=i['id'], first_name=i['first_name'],
                    last_name=i['last_name'],
                    age=i['age'], email=i['email'], role=i['role'],
                    phone=i['phone'])
        made_data.append(user)
    return made_data


def make_data_offers(data_list):
    made_data = []
    for i in data_list:
        offer = Offer(id=i['id'], order_id=i['order_id'], executor_id=i['executor_id'])
        made_data.append(offer)
    return made_data


def make_data_orders(data_list):
    made_data = []
    for i in data_list:
        order = Order(id=i['id'], name=i['name'],
                      description=i['description'], start_date=i['start_date'],
                      end_date=i['end_date'], address=i['address'],
                      price=i['price'], customer_id=i['customer_id'],
                      executor_id=i['executor_id'])
        made_data.append(order)
    return made_data


def take_data():
    users = make_data_users(get_json_data('users.json'))
    orders = make_data_orders(get_json_data('orders.json'))
    offers = make_data_offers(get_json_data('offers.json'))
    with db.session.begin():
        db.session.add_all(users)
        db.session.add_all(orders)
        db.session.add_all(offers)


def get_users():
    result = []
    users = db.session.query(User).all()
    for user in users:
        result.append({'id': user.id, 'first_name': user.first_name,
                       'last_name': user.last_name,
                       'age': user.age, 'email': user.email, 'role': user.role,
                       'phone': user.phone})
    return result


def get_users():
    result = []
    users = db.session.query(User).all()
    for user in users:
        result.append({'id': user.id, 'first_name': user.first_name,
                       'last_name': user.last_name,
                       'age': user.age, 'email': user.email, 'role': user.role,
                       'phone': user.phone})
    return result


def get_user_by_id(id):
    user = db.session.query(User).get(id)
    result = {'id': user.id, 'first_name': user.first_name,
              'last_name': user.last_name,
              'age': user.age, 'email': user.email, 'role': user.role,
              'phone': user.phone}
    return result


def get_orders():
    result = []
    orders = db.session.query(Order).all()
    for order in orders:
        result.append({'id': order.id, 'name': order.name,
                       'description': order.description,
                       'start_date': order.start_date, 'end_date': order.end_date,
                       'address': order.address,
                       'price': order.price, 'customer_id': order.customer_id,
                       'executor_id': order.executor_id})
    return result

def get_order(id):
    order = db.session.query(Order).get(id)
    result = {'id': order.id, 'name': order.name,
                       'description': order.description,
                       'start_date': order.start_date, 'end_date': order.end_date,
                       'address': order.address,
                       'price': order.price, 'customer_id': order.customer_id,
                       'executor_id': order.executor_id}
    return result
