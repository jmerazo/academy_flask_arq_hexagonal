class CreateStudents():
    def __init__(self, mysql):
        self.mysql = mysql

    def create(self, uid, names, lastnames, phone, email, semester):
        cursor = self.mysql.get_db().cursor()
        cursor.execute('INSERT INTO students (uid,names,lastnames,phone,email,semester) VALUES (%s,%s,%s,%s,%s,%s)',
                       (uid, names, lastnames, phone, email,semester,))
        self.mysql.get_db().commit()
        cursor.close()