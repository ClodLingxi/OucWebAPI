from logging import Logger

import re
import requests
from bs4 import BeautifulSoup

from ouc_course_tool.config import FetcherConfig
from ouc_course_tool.data import Course

class CourseFetcher:
    def __init__(self, config=None):
        self.config: FetcherConfig = config
        self.logger = Logger(self.__class__.__name__)

    def get_raw_html_request(self):
        result = requests.post(self.config.get_url(), headers=self.config.get_headers(), params=self.config.get_params())
        return result.text

    def get_page_total_count(self, raw_html=None):
        self.config.set_page_current()

        if raw_html is None:
            raw_html = self.get_raw_html_request()
        soup = BeautifulSoup(raw_html, 'html.parser')
        pagination_div = soup.find('div', {'class': 'pagination'})
        if pagination_div is None:
            return None
        reload_script = pagination_div.find_all('script')[1]
        match = re.search(r'\breloadPage\(.+?,(\d+),\d+\);', str(reload_script))
        return int(str(reload_script)[match.start(1)])



    def get_courses(self, page_current=1, raw_html=None):
        self.config.set_page_current(page_current)

        raw_courses_list = self._get_raw_courses_list(raw_html)
        return self._courses_format(raw_courses_list)

    def _courses_format(self, raw_courses_list):
        if not raw_courses_list:
            self.logger.info('Can not get raw courses list')
            return []

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
            raw_html = self.get_raw_html_request()
        soup = BeautifulSoup(raw_html, 'html.parser')
        table = soup.find('table')

        if table is None:
            return None
        rows = []
        for row in table.find_all('tr', class_=lambda value: value in ['E', 'O']):
            cells = [cell.get_text(strip=True) for cell in row.find_all(name='td', attrs=cell_attrs)]
            rows.append(cells)

        return rows
