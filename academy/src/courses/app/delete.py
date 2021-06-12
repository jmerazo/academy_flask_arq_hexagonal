from src.courses.domain.delete import DeleteCourses

class DeleteCoursesCase:
    def __init__(self, mysql):
        self.mysql = mysql

    def delete(self, id):
        deleteCourses = DeleteCourses(self.mysql)
        return deleteCourses.delete(id)