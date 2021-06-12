from src.sessions.domain.delete import DeleteSessions

class DeleteSessionsCase:
    def __init__(self, mysql):
        self.mysql = mysql

    def delete(self, id):
        deleteSessions = DeleteSessions(self.mysql)
        return deleteSessions.delete(id)