class CreateCourses():
    def __init__(self, mysql):
        self.mysql = mysql

    def create(self, name, semester):
        cursor = self.mysql.get_db().cursor()
        cursor.execute('INSERT INTO courses (name,semester) VALUES (%s,%s)',(name, semester,))
        self.mysql.get_db().commit()
        cursor.close()