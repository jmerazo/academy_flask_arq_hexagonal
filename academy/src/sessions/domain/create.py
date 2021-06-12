class CreateSessions():
    def __init__(self, mysql):
        self.mysql = mysql

    def create(self, course, date, starttime, endtime):
        cursor = self.mysql.get_db().cursor()
        cursor.execute('INSERT INTO sessions (course_id,date,start_time,end_time) VALUES (%s,%s,%s,%s)',
                       (course, date, starttime, endtime,))
        self.mysql.get_db().commit()
        cursor.close()