class DeleteStudents():
    def __init__(self, mysql):
        self.mysql = mysql

    def delete(self, id):
        cursor = self.mysql.get_db().cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", (id,))
        self.mysql.get_db().commit()
        cursor.close()