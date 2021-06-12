from src.students.domain.list import ListStudents

class ListStudentsCase:
    def __init__(self, mysql):
        self.mysql = mysql

    def list(self):
        listStudents = ListStudents(self.mysql)
        return listStudents.list()

    def search_student(self, id):
        listStudents = ListStudents(self.mysql)
        return listStudents.search_student(id)