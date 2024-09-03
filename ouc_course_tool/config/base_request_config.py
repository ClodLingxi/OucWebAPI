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
            return {
                "referer": self._referer,
                "user-agent": self._user_agent
            }
        return {
            "cookie": "JSESSIONID=" + self._session_id,
            "referer": self._referer,
            "user-agent": self._user_agent
        }

    def set_params(self, params):
        if type(params) is not dict:
            params = params.to_dict()
        self._params = params

    def get_params(self):
        return self._params

    def get_url(self):
        return self._base_url

    def set_session_id(self, session_id):
        self._session_id = session_id

    def get_session_id(self):
        return self._session_id
