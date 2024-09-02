# 使用方法
LoginConfig 配置用户名和密码
AccountValidation 由 LoginConfig 构造
Session_id 从 AccountValidation 的 get_login_session_id 方法获取

FetcherParams 配置查询参数
FetcherConfig 配置Session_id和配置查询参数(需要将FetcherParams类转为字典形式)
CourseFetcher 由 FetcherConfig构建

课程结果由 CourseFetcher 的 get_courses方法获取
