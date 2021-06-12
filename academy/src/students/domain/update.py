class UpdateStudents():
    def __init__(self, mysql):
        self.mysql = mysql

    def update(self, uid, names, lastnames, phone, email, semester, id):
        cursor = self.mysql.get_db().cursor()
        cursor.execute("UPDATE students SET uid = %s, names = %s, lastnames = %s, phone = %s, email = %s, semester = %s WHERE id = %s", (uid, names, lastnames, phone, email, semester, id,))
        self.mysql.get_db().commit()
        cursor.close()