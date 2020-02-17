from flask import render_template, Blueprint, url_for, redirect, flash, request, jsonify
from project.server.models import Books
from project.server import db

books_blueprint = Blueprint("books", __name__)


def get_books():
    books = Books.query.all()
    return jsonify(books=[b.serialize for b in books])

def make_books(title, author, genre):
    book = Books(title=title, author=author, genre=genre)
    db.session.add(book)
    db.session.commit()
    get_books()
    books = Books.query.all()
    return jsonify(books=[b.serialize for b in books])

def delete_book(id):
    book = Books.query.filter_by(id=int(id)).one()
    db.session.delete(book)
    db.session.commit()

    books = Books.query.all()
    return jsonify(books=[b.serialize for b in books])
def update_book(id):
    book = Books.query.filter_by(id=int(id)).one()
    book.title = 'Nuevo Valor2'
    db.session.commit()

    books = Books.query.all()
    return jsonify(books=[b.serialize for b in books])

@books_blueprint.route("/books", methods=["GET", "POST", "DELETE", "PUT"])
def booksfuntion():
   if request.method == 'GET':
        return get_books()
   elif request.method == 'POST':
       title = request.args.get('title')
       author = request.args.get('author')
       genre = request.args.get('genre')
       print(request.args)
       return make_books(title, author, genre)
   elif request.method == 'PUT':
       id = request.args.get('id')
       return update_book(id)
   else:
       id = request.args.get('id')
       return delete_book(id)
