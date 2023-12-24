from flask import Blueprint, request, render_template
from config import db, Region, CarTaxParam

car = Blueprint('car', __name__)


#  endpoint для внесения данных по налогу
@car.route('/v1/car/tax-param/add', methods=['POST'])
def add():
    data = request.form
    region_code = data['region_code']
    from_hp_car = data['from_hp_car']
    to_hp_car = data['to_hp_car']
    from_production_year_car = data['from_production_year_car']
    to_production_year_car = data['to_production_year_car']
    rate = data['rate']
    car = list(map(lambda x: x.get_id(), CarTaxParam.query.all()))
    regions = list(map(lambda x: x.get_id(), Region.query.all()))
    if int(region_code) not in regions:
        return {'reason': 'No such id or rate...'}, 400
    else:
        new_data = CarTaxParam(region_code, from_hp_car, to_hp_car, from_production_year_car, to_production_year_car,
                               rate)
        db.session.add(new_data)
        db.session.commit()
        message = 'Параметры успешно добавлены!'
        return render_template('tax-param-add.html', message=message)


#  endpoint для обновления данных по автоналогу
@car.route('/v1/car/tax-param/update', methods=['POST'])
def update():
    data = request.form
    region_code = data['region_code']
    from_hp_car = data['from_hp_car']
    to_hp_car = data['to_hp_car']
    from_production_year_car = data['from_production_year_car']
    to_production_year_car = data['to_production_year_car']
    rate = data['rate']
    regions = list(map(lambda x: x.get_id(), Region.query.all()))
    if int(region_code) not in regions:
        return {'reason': 'No such id or rate...'}, 400
    else:
        new_data = CarTaxParam.query.filter_by(city_id=region_code).update(
            {'city_id': region_code, 'from_hp_car': from_hp_car, 'to_hp_car': to_hp_car,
             'from_production_year_car': from_production_year_car, 'to_production_year_car': to_production_year_car,
             'rate': rate})
        db.session.commit()
        message = 'Параметры успешно обновлены!'
        return render_template('tax-param-update.html', message=message)


#  endpoint для удаления данных по автоналогу
@car.route('/v1/car/tax-param/delete', methods=['POST'])
def delete():
    data = request.form
    code_rate = data['code_rate']
    car = list(map(lambda x: x.get_id(), CarTaxParam.query.all()))

    if int(code_rate) in car:

        new_data1 = CarTaxParam.query.filter_by(id=code_rate).delete()
        db.session.commit()
        message = 'Параметры успешно обновлены!'

        return render_template('tax-param-delete.html', message=message)
    else:
        error = 'Нет такого id!'
        return render_template('tax-param-delete.html', error=error)


@car.route('/v1/car/tax-param/get/all')
def fetch_all():
    if id is None:
        return {'ERROR': 'Incorrect data'}, 400
    tax_auto = list(map(lambda x: x.__repr__(), CarTaxParam.query.all()))
    return tax_auto, 200


@car.route('/web/tax-param/add', methods=['GET'])
def get_tax_param_add():
    return render_template('tax-param-add.html')


@car.route('/web/tax-param/update', methods=['GET'])
def get_tax_param_update():
    return render_template('tax-param-update.html')


@car.route('/web/tax-param/delete', methods=['GET'])
def get_tax_param_delete():
    return render_template('tax-param-delete.html')


@car.route('/web/tax-param', methods=['GET'])
def get_tax_param_get():
    car_tax_params = CarTaxParam.query.all()
    return render_template('tax-param-list.html', car_tax_params=car_tax_params)
