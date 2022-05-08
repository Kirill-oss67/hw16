from flask import Flask
from db_direction import db, take_data
from pages.pages import pages_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)

app.register_blueprint(pages_blueprint)
#
# with db.session().begin():  # первый шаг
#     db.create_all()  # создание таблиц по объявленным классам
#     db.session.commit()  # фиксирование таблиц

# take_data()         # 2 шаг заполнение таблиц данными







if __name__ == "__main__":
    app.run(debug=True)
