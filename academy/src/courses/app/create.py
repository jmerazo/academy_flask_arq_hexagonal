from src.courses.domain.create import CreateCourses

class CreateCoursesCase:
    def __init__(self, mysql):
        self.mysql = mysql

    def create(self, name, semester):
        createCourses = CreateCourses(self.mysql)
        return createCourses.create(name, semester)