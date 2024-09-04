import pickle
import unittest

from config import TableFetcherConfig
from config import LoginConfig

from core.account_validation import AccountValidation
from core.table_fetcher import TableFetcher
from data.courses import TableFetcherParams

from test_config import ConfigOfTest


class TestCourseFechter(unittest.TestCase):
    _TEST_FILE = "test_resource/test_course_result.html"
    _tesseract_cmd_path = 'D:/Tools/Tesseract/tesseract.exe'

    def setUp(self):
        self.config = ConfigOfTest('./test_resource/account_local.ini')

        self.fetcher = TableFetcher()
        self.fetcher.set_search_param(TableFetcherParams(xh=self.config.get_username()))

        self.login_config = LoginConfig(self.config.get_username(), self.config.get_password(),
                                        self._tesseract_cmd_path)
        self.account_validation = AccountValidation(self.login_config)

        session_id = self.account_validation.get_login_session_id()
        print("Session ID: ", session_id)
        self.fetcher.config.set_session_id(session_id)

    def test_get_html_raw(self):
        result = self.fetcher._get_raw_html_request()
        print(result)
        return result

    def test_raw_html_handle(self):
        raw_html = self.fetcher._get_raw_html_request()
        result = self.fetcher._get_table_list_from_raw(raw_html)
        for course in result:
            print(course)

    def test_get_table_courses(self):
        result = self.fetcher.get_table_course_list()
        for course in result:
            print(course)