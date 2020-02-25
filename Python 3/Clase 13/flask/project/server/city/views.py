from flask import render_template, Blueprint, url_for, redirect, flash, request, jsonify
from project.server.peewee_model import City
from peewee import *

### DB ####
POSTGRES_URL = 'salt.db.elephantsql.com'
POSTGRES_USER = 'qhpmvcxf'
POSTGRES_PW = 'KVyxuSnUjHqmS8cv87HmKljukR7IKAXA'
POSTGRES_DB = 'qhpmvcxf'


psql = PostgresqlDatabase(
    user=POSTGRES_USER,
    password=POSTGRES_PW,
    host=POSTGRES_URL,
    database=POSTGRES_DB,
)

city_blueprint = Blueprint("city", __name__)

@city_blueprint.route("/city", methods=["GET", "POST", "DELETE", "PUT"])
def city_view():
    # Recuperar restaurantes
    if request.method == 'GET':
        with psql:
            cities = City.select()
            return jsonify(cities=[c.serializer for c in cities])
    elif request.method == 'POST':
        with psql:
            name = request.args.get('name', '')
            countrycode = request.args.get('countrycode', '')
            district = request.args.get('district', '')
            poblacion = int(request.args.get('poblacion', ''))
            object_value = {
                'name': name,
                'countrycode': countrycode,
                'district': district,
                'poblacion': poblacion
            }
            City.create(**object_value)
            #City.create(name=name, countrycode=countrycode .... )

            cities = City.select()
            return jsonify(cities=[c.serializer for c in cities])
    elif request.method == 'DELETE':
        with psql:
            id_data = int(request.args.get('id'))

            obj = City.delete().where(City.id==id_data)
            #City.get(City.id==id_data).delete()
            obj.execute()
            cities = City.select()
            return jsonify(cities=[c.serializer for c in cities])
    else:
        with psql:
            name = request.args.get('name')
            id_data = int(request.args.get('id'))
            obj = City.update(name=name).where(City.id==id_data)
            obj.execute()
            cities = City.select()
            return jsonify(cities=[c.serializer for c in cities])
