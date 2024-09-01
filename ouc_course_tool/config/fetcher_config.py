class FetcherConfig:

    _DEFAULT_REFERER = "http://jwgl.ouc.edu.cn/student/wsxk.kcbcx.html?menucode=JW130414"
    _DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    _DEFAULT_BASE_URL = "http://jwgl.ouc.edu.cn/taglib/DataTable.jsp?tableId=6146"

    def __init__(self, cookie, params, referer=None, user_agent=None, base_url=None, ):
        self._cookie = cookie
        self._params = params
        self._referer = referer
        self._user_agent = user_agent
        self._base_url = base_url

    def get_headers(self):
        if self._cookie is None:
            return None
        return {
            "cookie": self._cookie,
            "referer": self._DEFAULT_REFERER if self._referer is None else self._referer,
            "user-agent": self._DEFAULT_USER_AGENT if self._user_agent is None else self._user_agent
        }

    def get_params(self):
        return self._params

    def get_url(self):
        if self._base_url is None:
            return self._DEFAULT_BASE_URL
        return self._base_url