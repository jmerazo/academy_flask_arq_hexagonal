class ValidateAssistance():
    def __init__(self, mysql):
        self.mysql = mysql

    def validate(self, ide, ida, assistance):
        cursor = self.mysql.get_db().cursor()
        cursor.execute('INSERT INTO assistances (student_id, session_id, assistance) VALUES (%s, %s,%s)',
                       (ide, ida, assistance,))
        self.mysql.get_db().commit()
        cursor.close()