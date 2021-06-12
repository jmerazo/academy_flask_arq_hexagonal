from src.students.domain.create import CreateStudents

class CreateStudentsCase:
    def __init__(self, mysql):
        self.mysql = mysql

    def create(self, uid, names, lastnames, phone, email, semester):
        createStudents = CreateStudents(self.mysql)
        return createStudents.create(uid, names, lastnames, phone, email, semester)