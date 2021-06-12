class ListAssistances():
    def __init__(self, mysql):
        self.mysql = mysql

    def list_assistance(self):
        cursor = self.mysql.get_db().cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        cursor.close()
        return students
    
    def list_assistance_course(self, course):
        cursor = self.mysql.get_db().cursor()
        cursor.execute('SELECT * FROM sessions WHERE course_id = %s', (course,))
        students = cursor.fetchall()
        cursor.close()
        return students
    
    def list_assistance_session(self, ida):
        cursor = self.mysql.get_db().cursor()
        cursor.execute('SELECT * FROM assistances WHERE session_id = %s', (ida,))
        assistance = cursor.fetchall()
        cursor.close()
        return assistance