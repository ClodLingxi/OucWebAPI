from config.base_request_config import BaseRequestConfig

class FetcherConfig(BaseRequestConfig):

    _DEFAULT_REFERER = "http://jwgl.ouc.edu.cn/student/wsxk.kcbcx.html?menucode=JW130414"
    _DEFAULT_BASE_URL = "http://jwgl.ouc.edu.cn/taglib/DataTable.jsp?tableId=6146"

    _DEFAULT_ID_REFERER = "http://jwgl.ouc.edu.cn/student/wsxk.axkhksxk.html?menucode=JW130410"
    _DEFAULT_ID_BASE_URL = "http://jwgl.ouc.edu.cn/jw/common/getCourseInfoByXkh.action"

    def __init__(self, session_id, params=None, referer=_DEFAULT_REFERER, base_url=_DEFAULT_BASE_URL):
        super(FetcherConfig, self).__init__(session_id, params, referer, base_url)
        self.id_base_url = self._DEFAULT_ID_BASE_URL
        self.id_referer = self._DEFAULT_ID_REFERER

    def set_page_current(self, page_current=1):
        if page_current > 1:
            self._referer = self._DEFAULT_BASE_URL
            self._base_url = self._DEFAULT_BASE_URL + "&currPageCount=" + str(page_current)
        else:
            self._referer = self._DEFAULT_REFERER
            self._base_url = self._DEFAULT_BASE_URL

    def set_id_sql_config(self, id_reference, id_base_url):
        self.id_referer = id_reference
        self.id_base_url = id_base_url