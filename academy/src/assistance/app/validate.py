from src.assistance.domain.validate import ValidateAssistance

class ValidateAssistanceCase:
    def __init__(self, mysql):
        self.mysql = mysql

    def validate(self, ide, ida, assistance):
        validateAssistance = ValidateAssistance(self.mysql)
        return validateAssistance.validate(ide, ida, assistance)