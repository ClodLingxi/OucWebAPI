from logging import Logger

import requests
from bs4 import BeautifulSoup

from config import TableFetcherConfig
from data import Course


class TableFetcher:
    def __init__(self, config=None):
        if config is None:
            config = TableFetcherConfig()
        self.config: TableFetcherConfig = config
        self.logger = Logger(self.__class__.__name__)

    def set_username(self, username):
        self.config._params.setdefault('xh', username)

    def set_search_param(self, params):
        self.config.set_params(params)

    def get_selection_number_list(self):
        return list(map(lambda course: course.selection_number, self.get_table_course_list()))

    def get_table_course_list(self) -> list[Course]:
        raw_list = self._get_table_list_from_raw()
        result_list = []
        for raw_course in raw_list:
            result_list.append(
                Course(course_name=raw_course[1],
                       campus=raw_course[5],
                       selection_number=raw_course[6],
                       instructor=raw_course[7],
                       notes=raw_course[13])
            )
        return result_list

    def _get_table_list_from_raw(self, raw_html=None):
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

    def _get_raw_html_request(self):
        result = requests.post(self.config.get_url(), headers=self.config.get_headers(),
                               params=self.config.get_params(), timeout=(10, 10))
        return result.text
