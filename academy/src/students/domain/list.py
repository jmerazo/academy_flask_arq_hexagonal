class ListStudents():
    def __init__(self, mysql):
        self.mysql = mysql

    def list(self):
        cursor = self.mysql.get_db().cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        cursor.close()
        return students
    
    def search_student(self, id):
        cursor = self.mysql.get_db().cursor()
        cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
        search = cursor.fetchone()
        cursor.close()
        return search