from flask import render_template, Blueprint, url_for, redirect, flash, request, jsonify
from project.server.pony import Restautants


restaurant_blueprint = Blueprint("restaurant", __name__)

def get_books():

    return jsonify(books=[b.serialize for b in books])

@restaurant_blueprint.route("/restaurant", methods=["GET", "POST", "DELETE", "PUT"])
def restaurant_view():
    if request.method == 'GET':
        get_books()

