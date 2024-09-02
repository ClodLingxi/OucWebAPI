class BaseRequestConfig:

    _DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

    def __init__(self, session_id, params, referer, base_url, user_agent=_DEFAULT_USER_AGENT):
        self._session_id = session_id
        self._params = params
        self._referer = referer
        self._base_url = base_url
        self._user_agent = user_agent

    def get_headers(self):
        if self._session_id is None:
            return None
        return {
            "cookie": "JSESSIONID=" + self._session_id,
            "referer": self._referer,
            "user-agent": self._user_agent
        }

    def get_headers(self, session_id):
        return {
            "cookie": "JSESSIONID=" + session_id,
            "referer": self._referer,
            "user-agent": self._user_agent
        }

    def get_params(self):
        return self._params

    def get_url(self):
        return self._base_url

    def get_session_id(self):
        return self._session_id
