import unittest
from bs4 import BeautifulSoup

from ouc_course_tool.config import FetcherConfig
from ouc_course_tool.core.course_fetcher import CourseFetcher
from ouc_course_tool.data import FetcherParams


class TestCourseFechter(unittest.TestCase):
    _COOKIE = "JSESSIONID=" + "F1072C84F4778E07E81A0EA90ED123FB"
    _QUERY_PARAM = FetcherParams(
        initQry=0, xktype=2, xh="[USERNAME]", xn="2024", xq=0, nj="2022", zydm="0143",
        items="", xnxq="2024-0", kcfw="Specialty", sel_nj="2022", sel_zydm="0143",
        sel_schoolarea="", sel_cddwdm="", sel_kc="", kcmc=""
    )
    def setUp(self):
        self.config = FetcherConfig(cookie=self._COOKIE, params=self._QUERY_PARAM.to_dict())
        self.fetcher = CourseFetcher(self.config)

    def test_fetcher_by_config(self):
        courses = self.fetcher.get_courses()
        for course in courses:
            print(course)

    _TEST_FILE = "test_resource/test_course_result.html"
    def test_html_raw_handle(self):
        with open(self._TEST_FILE, 'r', encoding='utf-8') as file:
            raw_html = file.read()
            courses = self.fetcher.get_raw_courses_list(raw_html)
            for course in courses:
                print(course)

    def test_fetcher_by_html(self):
        with open(self._TEST_FILE, 'r', encoding='utf-8') as file:
            raw_html = file.read()
            courses = self.fetcher.get_courses(raw_html)
            for course in courses:
                print(course)
