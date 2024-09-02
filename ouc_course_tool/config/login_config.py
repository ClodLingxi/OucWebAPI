from config.base_request_config import BaseRequestConfig

class LoginConfig(BaseRequestConfig):

    _DEFAULT_REFERER = "http://jwgl.ouc.edu.cn/cas/login.action"

    _DEFAULT_BASE_URL = "http://jwgl.ouc.edu.cn/cas/logon.action"
    _DEFAULT_CAPTCHA_URL = "http://jwgl.ouc.edu.cn/cas/genValidateCode"

    def __init__(self, username, password, session_id=None, params=None, referer=_DEFAULT_REFERER, base_url=_DEFAULT_BASE_URL):
        super(LoginConfig, self).__init__(session_id, params, referer, base_url)
        self._username = username
        self._password = password

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_headers(self):
        headers = super(LoginConfig, self).get_headers()

        return headers

    def get_captcha_headers(self):
        if self._session_id is None:
            return {
                "referer": self._DEFAULT_CAPTCHA_URL,
                "user-agent": self._user_agent
            }
        return {
            "cookie": "JSESSIONID=" + self._session_id,
            "referer": self._DEFAULT_CAPTCHA_URL,
            "user-agent": self._user_agent
        }