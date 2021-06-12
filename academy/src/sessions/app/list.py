from src.sessions.domain.list import ListSessions

class ListSessionsCase:
    def __init__(self, mysql):
        self.mysql = mysql

    def list_sessions_all(self):
        listSessions = ListSessions(self.mysql)
        return listSessions.list_sessions_all()
    
    def list_sessions_course(self, idc):
        listSessions = ListSessions(self.mysql)
        return listSessions.list_sessions_course(idc)