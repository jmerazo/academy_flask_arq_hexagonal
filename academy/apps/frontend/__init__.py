from flask import Flask, jsonify, request, redirect, url_for, render_template
from src.shared.infra.db import mysql
from src.students.app.list import ListStudentsCase
from src.students.app.create import CreateStudentsCase
from src.students.app.update import UpdateStudentsCase
from src.students.app.delete import DeleteStudentsCase
from src.courses.app.list import ListCoursesCase
from src.courses.app.create import CreateCoursesCase
from src.courses.app.delete import DeleteCoursesCase
from src.sessions.app.list import ListSessionsCase
from src.sessions.app.create import CreateSessionsCase
from src.sessions.app.delete import DeleteSessionsCase
from src.assistance.app.list import ListAssistancesCase
from src.assistance.app.validate import ValidateAssistanceCase

app = Flask(__name__)

############### INDEX ##################
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

############### STUDENTS ##################
@app.route('/students/list', methods=['GET'])
def list_students():
    listStudentsCase = ListStudentsCase(mysql)
    students = listStudentsCase.list()
    return render_template('students/list.html', students=students)

@app.route('/create_student_preview', methods=['POST', 'GET'])
def create_students_preview():
    return render_template('students/create.html')

@app.route('/students/create', methods=['POST'])
def create_students():
    createStudentsCase = CreateStudentsCase(mysql)
    uid = request.form['uid']
    names = request.form['names']
    lastnames = request.form['lastnames']
    phone = request.form['phone']
    email = request.form['email']
    semester = request.form['semester']
    createStudentsCase.create(uid, names, lastnames, phone, email, semester)
    return redirect(url_for('create_students_preview'))

@app.route('/update_student_preview/<id>', methods=['POST', 'GET'])
def update_student_preview(id):
    listStudentsCase = ListStudentsCase(mysql)
    student = listStudentsCase.search_student(id)
    id = student[0]
    uid = student[1]
    names = student[2]
    lastnames = student[3]
    phone = student[4]
    email = student[5]
    semester = student[6]

    return render_template('students/update.html', id=id, uid=uid, names=names, lastnames=lastnames, phone=phone, email=email, semester=semester)

@app.route('/update_student/<id>', methods=['PUT', 'GET', 'POST'])
def update_student(id):
    updateStudentsCase = UpdateStudentsCase(mysql)
    uid = request.form['uid']
    names = request.form['names']
    lastnames = request.form['lastnames']
    phone = request.form['phone']
    email = request.form['email']
    semester = request.form['semester']

    updateStudentsCase.update(uid, names, lastnames, phone, email, semester, id)
    return redirect(url_for('list_students'))

@app.route('/delete_student/<id>', methods=['POST', 'GET'])
def delete_student(id):
    deleteStudentsCase = DeleteStudentsCase(mysql)
    deleteStudentsCase.delete(id)
    return redirect(url_for('list_students'))

############### COURSES ##################
@app.route('/create_courses_preview')
def create_courses_preview():
    return render_template('courses/create.html')

@app.route('/create_courses', methods=['POST', 'GET'])
def create_courses():
    createCoursesCase = CreateCoursesCase(mysql)
    name = request.form['name']
    semester = request.form['semester']
    createCoursesCase.create(name, semester)

    return render_template('courses/create.html')

@app.route('/courses/list', methods=['GET'])
def list_courses():
    listCoursesCase = ListCoursesCase(mysql)
    courses = listCoursesCase.list()
    return render_template('courses/list.html', courses=courses)

@app.route('/course/delete/<id>', methods=['POST', 'GET'])
def delete_course(id):
    deleteCoursesCase = DeleteCoursesCase(mysql)
    deleteCoursesCase.delete(id)
    return redirect(url_for('list_courses'))

############### SESSIONS ##################
@app.route('/list_sessions', methods=['POST', 'GET'])
def list_sessions():
    listSessionsCase = ListSessionsCase(mysql)
    sessions = listSessionsCase.list_sessions_all()
    idc = []
    for s in range(len(sessions)):
        idc = sessions[s][4]
    return render_template('sessions/list.html', sessions=sessions)

@app.route('/create_session_preview', methods=['POST', 'GET'])
def create_session_preview():
    listCoursesCase = ListCoursesCase(mysql)
    courses = listCoursesCase.list()
    return render_template('sessions/create.html', courses=courses)

@app.route('/session/create', methods=['POST', 'GET'])
def create_session():
    createSessionsCase = CreateSessionsCase(mysql)
    course = request.form['course']
    date = request.form['date']
    starttime = request.form['starttime']
    endtime = request.form['endtime']

    createSessionsCase.create(course, date, starttime, endtime)
    return redirect(url_for('list_sessions'))

@app.route('/session/delete/<id>', methods=['POST', 'GET'])
def delete_session(id):
    deleteSessionsCase = DeleteSessionsCase(mysql)
    deleteSessionsCase.delete(id)
    return redirect(url_for('list_sessions'))

############### ASSISTANCE ##################
@app.route('/assistance/<ida>', methods=['POST', 'GET'])
def assistance_students(ida):
    listAssistancesCase = ListAssistancesCase(mysql)
    assistance = listAssistancesCase.list_assistance_course(ida)
    return render_template('assistance/list.html', assistance=assistance)

@app.route('/start_session', methods=['POST', 'GET'])
def start_session():
    listAssistancesCase = ListAssistancesCase(mysql)
    students = listAssistancesCase.list_assistance()
    return render_template('assistance/assistance.html', students=students)

@app.route('/assistance_validate/<ida>', methods=['POST', 'GET'])
def assistance_validate(ida):
    validateAssistanceCase = ValidateAssistanceCase(mysql)
    assistance = request.form['assistance']
    ide = request.form['ide']
    
    validateAssistanceCase.validate(ide, ida, assistance)
    return redirect(url_for('list_sessions'))

def create_app_frontend():
    app.run(debug=True, port=5000)