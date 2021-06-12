class ListCourses():
    def __init__(self, mysql):
        self.mysql = mysql

    def list (self):
        cursor = self.mysql.get_db().cursor()
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        cursor.close()
        return courses