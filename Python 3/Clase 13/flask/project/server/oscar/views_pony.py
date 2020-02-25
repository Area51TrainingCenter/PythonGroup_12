from flask import Blueprint, request, jsonify
from project.server.reto.pony import Country, UserOscar
from pony.orm import *
import random

oscar_blueprint = Blueprint("oscar", __name__)


def get_list_country():
    countries = Country.select(lambda Country: Country)
    return jsonify(country=[c.serializer for c in countries])


def get_list_user():
    users = UserOscar.select(lambda UserOscar: UserOscar)
    return jsonify(user=[u.serializer for u in users])


@oscar_blueprint.route("/country", methods=["GET", "POST"])
def country_view():
    if request.method == 'GET':
        with db_session:
            return get_list_country()
    else:
        with db_session:
            name = request.args.get('name', '')
            if name == '':
                return jsonify({'message': 'error'})
            else:
                Country(name=name)
                commit()
            return get_list_country()


@oscar_blueprint.route("/useroscar", methods=["GET", "POST"])
def useroscar_view():
    if request.method == 'GET':
        with db_session:
            return get_list_user()
    else:
        with db_session:
            name = request.args.get('name', '')
            last_name = request.args.get('last_name', '')
            countries = Country.select(lambda Country: Country)
            list_countries = list(countries)
            country = random.choice(list_countries)
            # list_empty = []
            # for country in countries:
            #     list_empty.append(country)
            UserOscar(name=name, last_name=last_name, country=country)
            commit()
            return get_list_user()
