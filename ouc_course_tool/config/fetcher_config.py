from config.base_request_config import BaseRequestConfig

class FetcherConfig(BaseRequestConfig):

    _DEFAULT_REFERER = "http://jwgl.ouc.edu.cn/student/wsxk.kcbcx.html?menucode=JW130414"
    _DEFAULT_BASE_URL = "http://jwgl.ouc.edu.cn/taglib/DataTable.jsp?tableId=6146"

    def __init__(self, session_id, params, referer=_DEFAULT_REFERER, base_url=_DEFAULT_BASE_URL):
        super(FetcherConfig, self).__init__(session_id, params, referer, base_url)