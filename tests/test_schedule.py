import pickle
import unittest

from data import Course
from ouc_course_tool.data.schedule import CourseTable

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.test_set_course_list()

    def test_set_course_list(self, course_list=None):
        if course_list is None:
            with open('get_courses_from_mul_params.pickle', 'rb') as file:
                self.course_list: list[list[Course]] = pickle.load(file)
        else:
            self.course_list: list[list[Course]] = course_list

    @staticmethod
    def is_in_course(target, course_list):
        for course in course_list:
            if course in target:
                return True

    def test_get_overflow_class(self):
        for courses in self.course_list:
            for course in courses:
                if int(course.limit) < int(course.selected_count):
                    print(course.course_name, course.limit, course.selected_count)

    def test_something(self, limit=True):
        self.test_set_course_list()

        importance_course = [
            # '概率统计',
            # '形势与政策',
            # '毛泽东思想',
            '离散数学',
            # '计算机系统基础',
            # '大学生职业发展教育',
            '人工智能导论',
            '机器人学导论',
        ]

        def limit_function(course: Course):
            # return False

            if self.is_in_course(course.course_name, importance_course):
                return False

            if float(course.limit) < int(course.selected_count) * 1:
                return True

            for time in course.get_class_time_list():
                if time.start_period == 1:
                    if self.is_in_course(course.course_name, importance_course):
                        return False
                    return True

        if limit:
            table: CourseTable = CourseTable.calculate_course(self.course_list, limit_function)
        else:
            table: CourseTable = CourseTable.calculate_course(self.course_list)
        table.print_courses()