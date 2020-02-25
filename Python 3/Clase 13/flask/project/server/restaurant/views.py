from flask import render_template, Blueprint, url_for, redirect, flash, request, jsonify
from project.server.pony_model import Restautants, Folks
from pony.orm import *


restaurant_blueprint = Blueprint("restaurant", __name__)


def serializer(obj):
    return {
        'name': obj.name,
        'owner': obj.owner,
        'folk': obj.folk
    }
@restaurant_blueprint.route("/restaurant", methods=["GET", "POST", "DELETE", "PUT"])
def restaurant_view():
    # Recuperar restaurantes
    if request.method == 'GET':
        with db_session:
            # Book.objects.all()
            # Book.query.all()
            restaurants_pony = Restautants.select(lambda Restautants: Restautants).order_by(desc(Restautants.id))
            return jsonify(resta=[serializer(r) for r in restaurants_pony])
    elif request.method == 'POST':
        with db_session:
            name = request.args.get('name', '')
            owner = request.args.get('owner', '')
            folk = request.args.get('folk', False)
            data_folk =Folks(
                            quantity=2
                       )
            Restautants(
                name=name,
                owner=owner,
                folk=folk,
                folks=data_folk
            )
            restaurants_pony = Restautants.select(lambda Restautants: Restautants).order_by((Restautants.id))
            return jsonify(resta=[serializer(r) for r in restaurants_pony])
    elif request.method == 'DELETE':
        with db_session:
            name = request.args.get('name', '')
            print(f'Este elemento sera eliminado {name}')
            Restautants.get(name=name).delete()
            commit()
            restaurants_pony = Restautants.select(lambda Restautants: Restautants).order_by((Restautants.id))
            return jsonify(resta=[serializer(r) for r in restaurants_pony])
    else:
        with db_session:
            id = request.args.get('id', '')
            print(f'Este elemento sera actualizado {id}')
            rest = Restautants.get(id=int(id))
            rest.name = 'Hola Mundo'
            rest.folk = False
            commit()
            restaurants_pony = Restautants.select(lambda Restautants: Restautants).order_by((Restautants.id))
            return jsonify(resta=[serializer(r) for r in restaurants_pony])


