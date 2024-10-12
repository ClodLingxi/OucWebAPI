import unittest

from PIL import Image

from ouc_course_tool.core.account_validation import AccountValidation
from ouc_course_tool.config import LoginConfig

ACCOUNT = {
    'username': '[USERNAME]',
    'password': '[PASSWORD]',
}

class TestAccountValidation(unittest.TestCase):
    _CAPTCHA_TEMP_PATH = "test_resource/test_account_captcha.png"
    _TEST_SESSION_ID = 'B718EB30FE1D875E4C5494C228781775'
    _LOGIN_CONFIG = LoginConfig(ACCOUNT['username'], ACCOUNT['password'])

    def setUp(self):
        self.account_validation = AccountValidation(config=self._LOGIN_CONFIG)

    def set_session_id(self):
        self.account_validation.config.set_session_id(self._TEST_SESSION_ID)

    def test_encode_logic(self):
        encoded_username, hashed_password = (self.account_validation._get_encoded_username_and_password
                                            (username=ACCOUNT['username'],
                                            password=ACCOUNT['password'],
                                            session_id=self._TEST_SESSION_ID,
                                            rand_number="asda"))
        print(encoded_username, hashed_password)

    def test_get_captcha_and_recognize(self):
        captcha, _ = self.account_validation.get_raw_captcha_and_session_id()
        with open(self._CAPTCHA_TEMP_PATH, "wb") as file:
            file.write(captcha)
            file.close()
        image = Image.open(self._CAPTCHA_TEMP_PATH)
        text = self.account_validation._recognize_captcha(image)
        print(text)

    def test_get_session_id(self):
        self.set_session_id()

        _, session_id = self.account_validation.get_raw_captcha_and_session_id()
        print(session_id)

    def test_get_rand_number_and_session_id(self):
        rand_number, session_id = self.account_validation.get_rand_number_and_session_id()
        print(rand_number, session_id)

    def test_login_raw_result_with_session_id(self):
        self.set_session_id()

        result, session_id = self.account_validation._get_login_raw_result_and_session_id()
        print("SESSION_ID: " + session_id, result)

    def test_login_raw_result_and_session_id(self):
        result, session_id = self.account_validation._get_login_raw_result_and_session_id()
        print(type(result), result, result.get('message'))

    def test_login(self):
        session_id = self.account_validation.get_login_session_id()
        print(session_id)