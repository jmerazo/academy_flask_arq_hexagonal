from src.assistance.domain.list import ListAssistances

class ListAssistancesCase:
    def __init__(self, mysql):
        self.mysql = mysql

    def list_assistance(self):
        listAssistances = ListAssistances(self.mysql)
        return listAssistances.list_assistance()
    
    def list_assistance_course(self, course):
        listAssistances = ListAssistances(self.mysql)
        return listAssistances.list_assistance_course(course)
    
    def list_assistance_session(self, ida):
        listAssistances = ListAssistances(self.mysql)
        return listAssistances.list_assistance_course(ida)