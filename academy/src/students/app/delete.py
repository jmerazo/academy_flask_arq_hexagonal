from src.students.domain.delete import DeleteStudents

class DeleteStudentsCase:
    def __init__(self, mysql):
        self.mysql = mysql

    def delete(self, id):
        deleteStudents = DeleteStudents(self.mysql)
        return deleteStudents.delete(id)