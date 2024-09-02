from ouc_course_tool import *
from tests.test_config import ConfigOfTest

if __name__ == '__main__':
    test_config = ConfigOfTest('./tests/test_resource/account_local.ini')

    login_config = LoginConfig(test_config.get_username(), test_config.get_password())
    session_id = AccountValidation(login_config).get_login_session_id()

    fetcher_params = FetcherParams(
        initQry=0, xktype=2, xh="", xn="2024", xq=0, nj="2022", zydm="0143",
        items="", xnxq="2024-0", kcfw="Specialty", sel_nj="2022", sel_zydm="0143",
        sel_schoolarea=""
    ).to_dict()
    fetcher_config = FetcherConfig(session_id=session_id, params=fetcher_params)
    course_fetcher = CourseFetcher(config=fetcher_config)

    fetcher_result = course_fetcher.get_courses()

    for course in fetcher_result:
        print(course)

