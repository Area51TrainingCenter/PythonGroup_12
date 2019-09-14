from flask import render_template, Blueprint, url_for, redirect, flash, request
from project.server.models import Students
from project.server import db


student_blueprint = Blueprint("students", __name__)


@student_blueprint.route("/stu",)
def home_students():
    return render_template('student/students.html', students=Students.query.all())


@student_blueprint.route('/newstudent', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Error','error')
        else:
            student = Students(request.form['name'], request.form['city'],
                               request.form['addr'], request.form['pin'])
            db.session.add(student)
            db.session.commit()

            return redirect('/students')
    return render_template('new.html')
