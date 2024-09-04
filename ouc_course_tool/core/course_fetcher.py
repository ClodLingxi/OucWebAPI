from logging import Logger

import re
import requests
from bs4 import BeautifulSoup

from ouc_course_tool.config import CourseFetcherConfig
from ouc_course_tool.data import Course


class CourseFetcher:
    def __init__(self, config=None):
        self.config: CourseFetcherConfig = config
        self.logger = Logger(self.__class__.__name__)

    def set_search_param(self, params):
        self.config.set_params(params)

    def _get_raw_html_request(self):
        # print("Start get html " + str(self.config.get_url()))
        result = requests.post(self.config.get_url(), headers=self.config.get_headers(),
                               params=self.config.get_params(), timeout=(10, 10))
        # print("End get html " + str(self.config.get_url()))
        return result.text

    def _get_page_total_count(self, raw_html=None):
        self.config.set_page_current()

        if raw_html is None:
            raw_html = self._get_raw_html_request()
        soup = BeautifulSoup(raw_html, 'html.parser')
        pagination_div = soup.find('div', {'class': 'pagination'})
        if pagination_div is None:
            return None
        reload_script = pagination_div.find_all('script')[1]
        match = re.search(r'\breloadPage\(.+?,(\d+),\d+\);', str(reload_script))
        return int(str(reload_script)[match.start(1)])

    def get_course_by_selection_id(self, selection_id, xn='2024', xq='1', xh=''):
        param = {
            "xkh": selection_id,
            "xn": xn,
            "xq": xq,
            "xh": xh,
            "hidOption": "qry"
        }
        result = requests.post(self.config.id_base_url, headers=self.config.get_headers(),
                               params=param, timeout=(10, 10)).json()
        return result

    def _get_courses_from_page_current(self, page_current=1, raw_html=None):
        self.config.set_page_current(page_current)

        raw_courses_list = self._get_raw_courses_list(raw_html)
        return self._courses_format(raw_courses_list)

    def _get_all_courses_from_all_page(self):
        page_count_result = self._get_page_total_count()

        result = []
        for page_current in range(1, page_count_result + 1):
            fetcher_result: list = self._get_courses_from_page_current(page_current)
            result.append(fetcher_result)

        return result

    def get_courses_by_params(self, params=None):
        self.config.set_params(params)
        result = self._get_courses_from_page_current()
        return result

    def get_courses_from_mul_params(self, params_list):
        result = []
        for params in params_list:
            self.config.set_params(params)
            temp = self._get_all_courses_from_all_page()
            result += temp
        return result

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
                    Course(raw_courses[0], raw_courses[1], raw_courses[2], raw_courses[3], raw_courses[4],
                           raw_courses[5], raw_courses[6], raw_courses[7], raw_courses[8], raw_courses[9],
                           raw_courses[10], raw_courses[11], raw_courses[12], raw_courses[13], raw_courses[14],
                           raw_courses[15])
                )
        return courses_list

    def _get_raw_courses_list(self, raw_html=None):
        cell_attrs = {'style': ''}
        if raw_html is None:
            raw_html = self._get_raw_html_request()
        soup = BeautifulSoup(raw_html, 'html.parser')
        table = soup.find('table')

        if table is None:
            return None
        rows = []
        for row in table.find_all('tr', class_=lambda value: value in ['E', 'O']):
            cells = [cell.get_text(strip=True) for cell in row.find_all(name='td', attrs=cell_attrs)]
            rows.append(cells)

        return rows
