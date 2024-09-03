from symtable import Function
from typing import Callable

from PIL.Image import preinit

from data import Course, ScheduleFormat

class CourseTable:
    def __init__(self):
        self.selected_courses: list[Course] = []


    def add_course(self, course):
        self.selected_courses.append(course)

    def pop_course(self):
        self.selected_courses.pop()

    def is_conflict(self, course: Course) -> bool:
        for selected_course in self.selected_courses:
            for selected_schedule in selected_course.get_class_time_list():
                if selected_schedule.conflicts_with_list(course.get_class_time_list()):
                    return True
        return False

    def print_courses(self):
        for selected_course in self.selected_courses:
            print(selected_course.course_name)
            print(selected_course.selection_number, selected_course.get_class_time_list())
            print()

    @staticmethod
    def calculate_course(select_course_list: list[list[Course]], limit_function: Callable[[Course], bool] = None):
        table = CourseTable()

        course_list_index_list = [0] * len(select_course_list)
        selected_course_index = 0
        while selected_course_index < len(select_course_list):
            selected_course = select_course_list[selected_course_index]
            flag = False
            for course_index in range(course_list_index_list[selected_course_index], len(selected_course)):
                course = selected_course[course_index]

                if limit_function is not None and limit_function(course):
                    continue

                if not table.is_conflict(course):
                    table.add_course(course)
                    course_list_index_list[selected_course_index] = course_index + 1
                    selected_course_index += 1
                    flag = True
                    break

            if not flag:
                table.pop_course()
                course_list_index_list[selected_course_index] = 0
                selected_course_index -= 1

        return table
