from flask import Flask, jsonify, request, redirect, url_for, render_template
from src.shared.infra.db import mysql
from src.students.app.list import ListStudentsCase
from src.students.app.create import CreateStudentsCase

app = Flask(__name__, template_folder='views')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/students', methods=['GET'])
def list_students():
    listStudentsCase = ListStudentsCase(mysql)
    return jsonify(listStudentsCase.run())

@app.route('/students/create', methods=['POST'])
def create_students():
    createStudentsCase = CreateStudentsCase(mysql)
    uid = request.form['uid']
    names = request.form['names']
    lastnames = request.form['lastnames']
    phone = request.form['phone']
    email = request.form['email']
    semester = request.form['semester']
    createStudentsCase.save(uid, names, phone, email,semester)
    return redirect(url_for('createStudentPreview'))

def create_app_api():
    app.run(debug=True, port=5100)