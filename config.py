from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/LAB_4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def __repr__(self):
        return f'<Region ID: {self.id}; Region name: {self.name}>'


class CarTaxParam(db.Model):
    __tablename__ = 'car_tax_param'
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('region.id', ondelete='CASCADE'))
    from_hp_car = db.Column(db.Integer, nullable=False)
    to_hp_car = db.Column(db.Integer, nullable=False)
    from_production_year_car = db.Column(db.Integer, nullable=False)
    to_production_year_car = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)

    def __init__(self, city_id, from_hp_car, to_hp_car, from_production_year_car, to_production_year_car, rate):
        self.city_id = city_id
        self.from_hp_car = from_hp_car
        self.to_hp_car = to_hp_car
        self.from_production_year_car = from_production_year_car
        self.to_production_year_car = to_production_year_car
        self.rate = rate

    def __repr__(self):
        return (f' city_id {self.city_id};'
                f' from_hp_car {self.from_hp_car};'
                f' to_hp_car {self.to_hp_car};'
                f' from_production_year_car {self.from_production_year_car};'
                f' to_production_year_car {self.to_production_year_car};'
                f' rate {self.rate}>')

    # функция для получения сухих данных автоналога из бд
    def get_data_for_rate(self):
        return self.id, self.city_id, self.from_hp_car, self.to_hp_car, self.from_production_year_car, self.to_production_year_car, self.rate

    # функция для получения айди автоналога из бд
    def get_id(self):
        return self.id


class AreaTaxParam(db.Model):
    __tablename__ = 'area_tax_param'
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('region.id', ondelete='CASCADE'))
    rate = db.Column(db.Integer, nullable=False)

    def __init__(self, id, city_id, rate):
        self.id = id
        self.city_id = city_id
        self.rate = rate

    def __repr__(self):
        return f'<AreaTaxParam {self.id}; city_id {self.city_id}; rate {self.rate}>'

    # функция для получения айди желищного налога
    def get_id(self):
        return self.id

    # функция для получения ставки желищного налога
    def get_data_for_rate(self):
        return self.rate


# def create_database():
with app.app_context():
    db.create_all()
