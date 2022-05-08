from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils import get_json_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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


def make_db():
    db.create_all()  # создание таблиц по объявленным классам
    db.session.commit()  # фиксирование таблиц


# make_db()  # первый шаг


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


# users = make_data_users(get_json_data('users.json'))
#
# with db.session.begin():
#     db.session.add_all(users)


# orders = make_data_orders(get_json_data('orders.json'))
#
# with db.session.begin():
#     db.session.add_all(orders)

# offers = make_data_offers(get_json_data('offers.json'))
#
# with db.session.begin():
#     db.session.add_all(offers)   # 2 шаг заполнение таблиц данными
