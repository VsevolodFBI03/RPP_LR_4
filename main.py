from region_routes import region
from tax_param_route import car
from tax_route import tax_route
from config import app
import argparse

parser = argparse.ArgumentParser

# регистрируем приложения
app.register_blueprint(region)
app.register_blueprint(car)
app.register_blueprint(tax_route)


@app.route('/favicon.ico')
def favicon():
    return ''


if __name__ == '__main__':
    # parser.add_argument('-c', '--create', action='create_database')
    app.run(debug=True)
