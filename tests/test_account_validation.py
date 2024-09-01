import unittest

from PIL import Image

from ouc_course_tool.core.account_validation import AccountValidation
from ouc_course_tool.config.login_config import LOGIN_CONFIG

class TestAccountValidation(unittest.TestCase):
    _CAPTCHA_PATH = "test_resource/test_account_captcha.png"

    def setUp(self):
        self.account_validation = AccountValidation(config=LOGIN_CONFIG)

    def test_get_captcha_and_recognize(self):
        captcha, _ = self.account_validation._get_raw_captcha_and_session()
        with open(self._CAPTCHA_PATH, "wb") as file:
            file.write(captcha)
            file.close()
        image = Image.open(self._CAPTCHA_PATH)
        text = AccountValidation._recognize_captcha(image)
        print(text)

    def test_get_cookies(self):
        _, cookies = self.account_validation._get_raw_captcha_and_session()
        print(cookies.values()[0])

    def test_get_rand_number_and_session_id(self):
        rand_number, session_id = self.account_validation.get_rand_number_and_session_id()
        print(rand_number, session_id)

    def test_login_raw_result(self):
        pass