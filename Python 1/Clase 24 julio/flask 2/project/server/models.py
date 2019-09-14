# project/server/models.py


import datetime

from flask import current_app

from project.server import db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, current_app.config.get("BCRYPT_LOG_ROUNDS")
        ).decode("utf-8")
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return "<User {0}>".format(self.email)


class Students(db.Model):

    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


class Client(db.Model):

    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), name="Nombre", nullable=False)
    last_name = db.Column(db.String(50), name="Apellido", nullable=False)
    number = db.Column(db.String(50), name="Numero de Telefono", nullable=False)

    def __init__(self, name, last_name, number):
        self.name = name
        self.last_name = last_name
        self.number = number


class Product(db.Model):

    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), name="Nombre", nullable=False)
    price_pen = db.Column(db.Float, name="Precio")
    price_dollar = db.column(db.Float, name="Precio")


class Orden(db.Model):

    __tablename__ = "orden"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.column(db.String(50), name="Nombre")
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    client = db.relationship("Client", backref=db.backref("client", uselist=False))
    product_id = db.column(db.Integer, db.ForeignKey("product.id"))
    product = db.relationship("Product", backref=db.backref("product", uselist=False)
