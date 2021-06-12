from src.students.domain.update import UpdateStudents

class UpdateStudentsCase:
    def __init__(self, mysql):
        self.mysql = mysql

    def update(self, uid, names, lastnames, phone, email, semester, id):
        updateStudents = UpdateStudents(self.mysql)
        return updateStudents.update(uid, names, lastnames, phone, email, semester, id)