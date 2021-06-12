from src.courses.domain.list import ListCourses

class ListCoursesCase:
    def __init__(self, mysql):
        self.mysql = mysql

    def list(self):
        listCourses = ListCourses(self.mysql)
        return listCourses.list()