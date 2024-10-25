import pickle
import unittest

import tests.test_schedule
from config import CourseFetcherConfig
from config import LoginConfig
from core import search_param_handle

from core.course_fetcher import CourseFetcher
from core.account_validation import AccountValidation
from data import CourseFetcherParams

from test_config import ConfigOfTest

class TestCourseFechter(unittest.TestCase):
    _TEST_FILE = "test_resource/test_course_result.html"
    _tesseract_cmd_path = 'D:/Tools/Tesseract/tesseract.exe'
    _TEST_SESSION_ID = "F1072C84F4778E07E81A0EA90ED123FB"
    _TEST_TEMP = '''
    {
    'zc':"1-17'，'sksj':·1-17周三(3-4节)"，'xm""唐瑞春"，'dyrkjs':'t0001118''3'，'fibh':*南489/410(94)'，
    "kcdm':'888583101221'，'xkrssx’:55,'skfs’:"讲授"，'adrs':85,'xqmc':'西海岸校区''rs':'55/85'，'kcmc':·计算机网络''khfs':'1'。'xf':'3.5'
    }
    ,
    {
    'zc':'1-5,7-17'，'sksj':'1-5,7-17周五(7-8节)'，'xm':'唐瑞春'，'dyrkjs':'t0001118"，'kclb2':'03','fjbh':'南404/403(131)',
    'kcdm':'080503101221'，'xkrssx':5"is kxcx':"日'，"Kc1b1':"01'.5，'skfs':'讲授''adrs':85、'xamc':'西海岸校区''rs':'55/85'、'kcmc'
    :'计算机网络','khfs':'1','xf':'3.5'
    }，
    {
    'zc':'14'，'sksj':'14周五(7-8节)双'，'xm':'唐瑞春'，'dyrkis':'t8801118','is kxcx':'@’，
    'kclb1':'81'，'kclb2':'83'，'fibh':'kcdm':'088583101221'，'xkrssx':55,'skfs':'讲授’，'qdrs':85,'xgmc":'西海岸校区'，'rs':'55/85'
    ，'kc'南404/403(131)'c':'计算机网络''khfs':'1'，'xf':'3.5'
    }
    ]
    '''
    _QUERY_PARAM = CourseFetcherParams(
        initQry=0, xktype=2, xh="", xn="2024", xq=0, nj="2022", zydm="0143",
        items="", xnxq="2024-0", kcfw="Specialty", sel_nj="2022", sel_zydm="0143",
        sel_schoolarea="", sel_cddwdm="", sel_kc="", kcmc=""
    )
    def setUp(self):
        self.config = ConfigOfTest('./test_resource/account_local.ini')

        self.fetcher_config = CourseFetcherConfig(session_id=self._TEST_SESSION_ID, params=self._QUERY_PARAM.to_dict())
        self.fetcher = CourseFetcher(self.fetcher_config)

        self.login_config = LoginConfig(self.config.get_username(), self.config.get_password(), self._tesseract_cmd_path)
        self.account_validation = AccountValidation(self.login_config)

        session_id = self.account_validation.get_login_session_id()
        self.fetcher.config.set_session_id(session_id)

    def test_html_raw_handle(self):
        with open(self._TEST_FILE, 'r', encoding='utf-8') as file:
            raw_html = file.read()
            courses = self.fetcher._get_raw_courses_list(raw_html)
            for course in courses:
                print(course)

    def test_fetcher_by_html(self):
        with open(self._TEST_FILE, 'r', encoding='utf-8') as file:
            raw_html = file.read()
            courses = self.fetcher._get_courses_from_page_current(raw_html)
            for course in courses:
                print(course)

    def test_fetcher_by_test_config(self):
        courses = self.fetcher._get_courses_from_page_current()
        for course in courses:
            print(course)

    def test_fetcher_by_login(self):

        session_id = self.account_validation.get_login_session_id()
        self.fetcher.config.set_session_id(session_id)

        courses = self.fetcher._get_courses_from_page_current()
        for course in courses:
            print(course)

    def test_total_page_fetcher(self):
        fetcher_params = CourseFetcherParams(
            xnxq="2024-1", kcfw="Specialty", sel_schoolarea="3", sel_kc="数值分析",
        ).to_dict()
        self.fetcher.config.set_params(fetcher_params)
        result = self.fetcher._get_all_courses_from_all_page()
        print(result)

    def test_mul_fetcher(self):
        target_course = [
            '概率-公共',
            '形势与政策-公共',
            '毛泽东思想-公共',
            '离散数学-智能科学-2023',
            '计算机系统基础-智能科学-2023',
            '人工智能导论-智能科学-2022',
            # '计算机图形学-智能科学-2022',
        ]
        select_params = search_param_handle.search_param_handle(target_course, 3, '2024-1')
        result = self.fetcher.get_courses_from_mul_params(select_params)

        with open('get_courses_from_mul_params.pickle', 'wb') as file:
            pickle.dump(result, file)

        test_module = tests.test_schedule.MyTestCase()
        test_module.test_something(limit=True)

    def test_get_course_by_id(self):
        result = self.fetcher.get_course_by_selection_id("19000017")
        print(result)
