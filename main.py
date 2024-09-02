from ouc_course_tool import *
from tests.test_config import ConfigOfTest

if __name__ == '__main__':
    # 格式在根目录下的 account.ini 文件中
    test_config = ConfigOfTest('./tests/test_resource/account_local.ini')

    # Tesseract 图片识别软件
    # EXAMPLE DOWNLOAD URL: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.4.20240503.exe
    tesseract_cmd_path = 'D:/Tools/Tesseract/tesseract.exe'

    login_config = LoginConfig(test_config.get_username(), test_config.get_password(), tesseract_cmd_path)
    session_id = AccountValidation(login_config).get_login_session_id()

    """ 样例
    xnxq="2024-1" 代表2024年第二个学期
    kcfw="Specialty" 代表专业课
    sel_nj="2023" 代表选课的年级 为2023级
    sel_zydm="0150" 代表选择的专业 为0150智能科学
    sel_schoolarea="3" 代表选择的校区 为西海岸校区
    """
    fetcher_params = FetcherParams(
        xnxq="2024-1", kcfw="Specialty", sel_nj="2023", sel_zydm="0150", sel_schoolarea="3"
    ).to_dict()

    fetcher_config = FetcherConfig(session_id=session_id, params=fetcher_params)
    course_fetcher = CourseFetcher(config=fetcher_config)

    fetcher_result = course_fetcher.get_courses()

    for course in fetcher_result:
        print(course.selection_number)
        print(course)

