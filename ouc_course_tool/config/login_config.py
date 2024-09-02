from config.base_request_config import BaseRequestConfig

class LoginConfig(BaseRequestConfig):

    _DEFAULT_REFERER = "http://jwgl.ouc.edu.cn/student/wsxk.kcbcx.html?menucode=JW130414"
    _DEFAULT_BASE_URL = "http://jwgl.ouc.edu.cn/taglib/DataTable.jsp?tableId=6146"

    def __init__(self, username, password, cookies , params=None, referer=_DEFAULT_REFERER, base_url=_DEFAULT_BASE_URL):
        super(LoginConfig, self).__init__(cookies, params, referer, base_url)
        self._username = username
        self._password = password

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password