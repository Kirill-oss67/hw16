from flask_sqlalchemy import SQLAlchemy
from util import get_json_data

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


def get_offers():
    result = []
    offers = db.session.query(Offer).all()
    for offer in offers:
        result.append({'id': offer.id, 'order_id': offer.order_id,
                       'executor_id': offer.executor_id})
    return result


def get_offer(id):
    offer = db.session.query(Offer).get(id)
    result = {'id': offer.id, 'order_id': offer.order_id,
              'executor_id': offer.executor_id}
    return result


def instance_to_dict(instance):
    return {
        "id": instance.id,
        "first_name": instance.first_name,
        "last_name": instance.last_name,
        "age": instance.age,
        "email": instance.email,
        "role": instance.role,
        "phone": instance.phone
    }


def create_user(data):
    user = User(
        id=data.get('id'),
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        age=data.get('age'),
        email=data.get('email'),
        role=data.get('role'),
        phone=data.get('phone'))

    db.session.add(user)
    db.session.commit()
    return instance_to_dict(user)


def update_user_by_id(id, data):
    user = db.session.query(User).get(id)
    setattr(user, 'first_name', data['first_name'])
    setattr(user, 'last_name', data['last_name']),
    setattr(user, 'age', data['age']),
    setattr(user, 'email', data['email']),
    setattr(user, 'role', data['role']),
    setattr(user, 'phone', data['phone']),
    db.session.add(user)
    db.session.commit()
    return instance_to_dict(db.session.query(User).get(id))


def delete_user(id):
    user = db.session.query(User).get(id)
    db.session.delete(user)
    db.session.commit()


def create_order(data):
    order = Order(
        name=data.get('name'),
        description=data.get('description'),
        start_date=data.get('start_date'),
        end_date=data.get('end_date'),
        address=data.get('address'),
        price=data.get('price'),
        customer_id=data.get('customer_id'),
        executor_id=data.get('executor_id'))
    db.session.add(order)
    db.session.commit()



def delete_order(id):
    order = db.session.query(Order).get(id)
    db.session.delete(order)
    db.session.commit()


def delete_offer(id):
    offer = db.session.query(Offer).get(id)
    db.session.delete(offer)
    db.session.commit()


def create_offer(data):
    offer = Offer(
        order_id=data.get('order_id'),
        executor_id=data.get('executor_id'))
    db.session.add(offer)
    db.session.commit()


def update_order_by_id(id, data):
    order = db.session.query(Order).get(id)
    setattr(order, 'name', data['name'])
    setattr(order, 'description', data['description']),
    setattr(order, 'start_date', data['start_date']),
    setattr(order, 'end_date', data['end_date']),
    setattr(order, 'address', data['address']),
    setattr(order, 'price', data['price']),
    setattr(order, 'customer_id', data['customer_id']),
    setattr(order, 'executor_id', data['executor_id'])
    db.session.add(order)
    db.session.commit()
    return 'updated'


def update_offer_by_id(id, data):
    offer = db.session.query(Offer).get(id)
    setattr(offer, 'order_id', data['order_id'])
    setattr(offer, 'executor_id', data['executor_id']),
    db.session.add(offer)
    db.session.commit()
    return 'updated'
