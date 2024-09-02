import unittest
from bs4 import BeautifulSoup


from config import FetcherConfig
from config import LoginConfig

from core.course_fetcher import CourseFetcher
from core.account_validation import AccountValidation
from data import FetcherParams

from test_account_validation import ACCOUNT

class TestCourseFechter(unittest.TestCase):
    _TEST_FILE = "test_resource/test_course_result.html"
    _TEST_SESSION_ID = "F1072C84F4778E07E81A0EA90ED123FB"
    _QUERY_PARAM = FetcherParams(
        initQry=0, xktype=2, xh="[USERNAME]", xn="2024", xq=0, nj="2022", zydm="0143",
        items="", xnxq="2024-0", kcfw="Specialty", sel_nj="2022", sel_zydm="0143",
        sel_schoolarea="", sel_cddwdm="", sel_kc="", kcmc=""
    )
    def setUp(self):
        self.fetcher_config = FetcherConfig(session_id=self._TEST_SESSION_ID, params=self._QUERY_PARAM.to_dict())
        self.fetcher = CourseFetcher(self.fetcher_config)

        self.login_config = LoginConfig(ACCOUNT['username'], ACCOUNT['password'])
        self.account_validation = AccountValidation(self.login_config)

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

    def test_fetcher_by_test_config(self):
        courses = self.fetcher.get_courses()
        for course in courses:
            print(course)

    def test_fetcher_by_login(self):

        session_id = self.account_validation.get_login_session_id()
        self.fetcher.config.set_session_id(session_id)

        courses = self.fetcher.get_courses()
        for course in courses:
            print(course)