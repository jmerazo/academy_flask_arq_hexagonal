class ListSessions():
    def __init__(self, mysql):
        self.mysql = mysql

    def list_sessions_all(self):
        cursor = self.mysql.get_db().cursor()
        cursor.execute("SELECT * FROM sessions")
        sessions = cursor.fetchall()
        cursor.close()
        return sessions
    
    def list_sessions_course(self, idc):
        cursor = self.mysql.get_db().cursor()
        cursor.execute("SELECT name FROM courses WHERE id = %s", (idc,))
        sessions_course = cursor.fetchall()
        cursor.close()
        return sessions_course