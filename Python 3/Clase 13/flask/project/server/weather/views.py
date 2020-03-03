from flask import Blueprint, request, jsonify
from project.server.pony_model import City, Localtion, WeatherDescription
from pony.orm import *
import requests
import json
import random

weather_blueprint = Blueprint("weather", __name__)


def get_list_city():
    cities = City.select(lambda City: City)
    return jsonify(user=[c.serializer for c in cities])


@weather_blueprint.route("/weather", methods=["GET", "POST"])
def weather_view():
    if request.method == 'GET':
        with db_session:
            return get_list_city()
    else:
        with db_session:
            city =  request.args.get('city')
            response = requests.get(f'http://api.weatherstack.com/current?access_key=c063f3676c65c5e3f40d19507248eb0d&query={city}')
            if response.status_code == 200:
                json_data = json.loads(response.content)
                Localtion()
                WeatherDescription()
                City()
            commit()
            return get_list_city()
