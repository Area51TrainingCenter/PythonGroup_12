from flask import Blueprint, request, jsonify
from project.server.reto.peewe import Category, psql, Movie
from peewee import *
import random

oscar_peewee_blueprint = Blueprint("oscar_peewee", __name__)


def get_category():
    categories = Category.select()
    return jsonify(categories=[c.serializer for c in categories])


@oscar_peewee_blueprint.route("/category", methods=["GET", "POST"])
def category_view():
    if request.method == 'GET':
        with psql:
            return get_category()
    else:
        name = request.args.get('name', '')
        if name == '':
            return jsonify({'message', 'error'})
        else:
            with psql:
                Category.create(name=name)
                return get_category()


def get_movie():
    movies = Movie.select()
    print(movies)
    return jsonify(movies=[m.serializer for m in movies])


@oscar_peewee_blueprint.route("/movie", methods=["GET", "POST"])
def movie_view():
    if request.method == 'GET':
        with psql:
            return get_movie()
    else:
        name = request.args.get('name', '')
        if name == '':
            return jsonify({'message', 'error'})
        else:
            with psql:
                categories = Category.select()
                print(categories)
                print('Paso 1')
                categories_list = list(categories)
                print(categories_list)
                print('Paso 2')
                category = random.choice(categories_list)
                print(category)
                print('Paso 3')
                Movie.create(name=name, category=category)
                return get_movie()
