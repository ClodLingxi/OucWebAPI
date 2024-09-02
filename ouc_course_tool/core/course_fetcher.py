import requests
from bs4 import BeautifulSoup

from ouc_course_tool.config import FetcherConfig
from ouc_course_tool.data import Course

class CourseFetcher:
    def __init__(self, config=None):
        self.config: FetcherConfig = config

    def get_courses(self, raw_html=None):
        raw_courses_list = self._get_raw_courses_list(raw_html)
        return self._courses_format(raw_courses_list)

    def _html_request(self):
        return (requests.
                post(self.config.get_url(), headers=self.config.get_headers(), params=self.config.get_params()).text)

    @staticmethod
    def _courses_format(raw_courses_list):
        class_time_index = -5

        courses_list = []
        for raw_courses in raw_courses_list:
            if raw_courses[0] == '' and raw_courses[class_time_index] == '':
                continue
            elif raw_courses[0] == '' and len(courses_list):
                courses_list[-1].add_class_time(raw_courses[class_time_index])
            else:
                courses_list.append(
                    Course(raw_courses[0],raw_courses[1],raw_courses[2],raw_courses[3],raw_courses[4],
                           raw_courses[5],raw_courses[6],raw_courses[7],raw_courses[8],raw_courses[9],
                           raw_courses[10],raw_courses[11],raw_courses[12],raw_courses[13],raw_courses[14],
                           raw_courses[15])
                )
        return courses_list


    def _get_raw_courses_list(self, raw_html=None):
        cell_attrs = {'style': ''}
        if raw_html is None:
            raw_html = self._html_request()
        soup = BeautifulSoup(raw_html, 'html.parser')
        table = soup.find('table')
        rows = []
        for row in table.find_all('tr', class_=lambda value: value in ['E', 'O']):
            cells = [cell.get_text(strip=True) for cell in row.find_all(name='td', attrs=cell_attrs)]
            rows.append(cells)
        return rows
