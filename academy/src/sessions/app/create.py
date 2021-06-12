from src.sessions.domain.create import CreateSessions

class CreateSessionsCase:
    def __init__(self, mysql):
        self.mysql = mysql

    def create(self, course, date, starttime, endtime):
        createSessions = CreateSessions(self.mysql)
        return createSessions.create(course, date, starttime, endtime)