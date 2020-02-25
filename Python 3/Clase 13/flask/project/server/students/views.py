from flask import render_template, Blueprint, url_for, redirect, flash, request
from project.server.models import Students
from project.server import db

student_blueprint = Blueprint("students", __name__)


@student_blueprint.route("/students")
def home_students():
    return render_template('student/students.html', students=Students.query.all())
