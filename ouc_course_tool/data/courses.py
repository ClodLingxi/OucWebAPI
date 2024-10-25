import re

class CourseFetcherParams:

    def __init__(self, initQry="0", xktype="2", xh="230000000", xn="2024", xq="1", nj="2023", zydm="0150", items="",
                 xnxq="2024-1", kcfw="Specialty",
                 sel_nj="2022", sel_zydm="0150", sel_schoolarea="", sel_cddwdm="", sel_kc="", kcmc=""):
        """
        :param initQry: 一般为0
        :param xktype: 选课类型
        :param xh: 学号， 为你的默认信息
        :param xn: 学年
        :param xq: 夏季学期为 0， 随时间递增递增
        :param nj: 年级， 为你的默认信息
        :param zydm: 专业编号， 为你的默认信息
        :param items: 一般为空
        :param xnxq: 学年和学期 例如：2024学年的秋季学期————2024-1 （其中2024-1为字符串内容）
        :param kcfw: 课程范围（PublicBasic 为公共课，Specialty 为专业课）
        :param sel_nj: 选择课程 所对应的 年级
        :param sel_zydm: 选择课程 所对应的 专业编号
        :param sel_schoolarea: 选择课程 所对应的 选课校区 从 0-3 其中 3 为西海岸
        :param sel_cddwdm: 开课单位
        :param sel_kc: 搜索关键字
        :param kcmc: 一般为空
        """
        self._sel_kc = None

        self.initQry = initQry
        self.xktype = xktype
        self.xh = xh
        self.xn = xn
        self.xq = xq
        self.nj = nj
        self.zydm = zydm
        self.items = items
        self.xnxq = xnxq
        self.kcfw = kcfw
        self.sel_nj = sel_nj
        self.sel_zydm = sel_zydm
        self.sel_schoolarea = sel_schoolarea
        self.sel_cddwdm = sel_cddwdm
        self.set_keyword(sel_kc)
        self.kcmc = kcmc

    def __repr__(self):
        return (f"QueryParameters(initQry={self.initQry}, xktype={self.xktype}, xh='{self.xh}', "
                f"xn='{self.xn}', xq={self.xq}, nj='{self.nj}', zydm='{self.zydm}', "
                f"items='{self.items}', xnxq='{self.xnxq}', kcfw='{self.kcfw}', "
                f"sel_nj='{self.sel_nj}', sel_zydm='{self.sel_zydm}', sel_schoolarea='{self.sel_schoolarea}', "
                f"sel_cddwdm='{self.sel_cddwdm}', sel_kc='{self._sel_kc}', kcmc='{self.kcmc}')")

    def set_keyword(self, sel_kc):
        self._sel_kc = sel_kc.encode('GB2312')

    def to_dict(self):
        return {
            "initQry": self.initQry,
            "xktype": self.xktype,
            "xh": self.xh,
            "xn": self.xn,
            "xq": self.xq,
            "nj": self.nj,
            "zydm": self.zydm,
            "items": self.items,
            "xnxq": self.xnxq,
            "kcfw": self.kcfw,
            "sel_nj": self.sel_nj,
            "sel_zydm": self.sel_zydm,
            "sel_schoolarea": self.sel_schoolarea,
            "sel_cddwdm": self.sel_cddwdm,
            "sel_kc": self._sel_kc,
            "kcmc": self.kcmc
        }

class TableFetcherParams:
    def __init__(
        self,
        xh: str = "23000010000", # 重要 学号
        electiveCourseForm_xktype: str = "2",
        electiveCourseForm_xn: str = "",
        electiveCourseForm_xq: str = "",
        electiveCourseForm_xh: str = "",
        electiveCourseForm_nj: str = "2022",
        electiveCourseForm_zydm: str = "0143",
        xqdm: str = "3",
        electiveCourseForm_kcdm: str = "",
        electiveCourseForm_kclb1: str = "",
        electiveCourseForm_kclb2: str = "",
        electiveCourseForm_khfs: str = "",
        electiveCourseForm_skbjdm: str = "",
        electiveCourseForm_xf: str = "",
        electiveCourseForm_is_buy_book: str = "",
        electiveCourseForm_is_cx: str = "",
        electiveCourseForm_is_yxtj: str = "",
        electiveCourseForm_xk_points: str = "",
        xn: str = "2024",
        xn1: str = "",
        _xq: str = "",
        xq_m: str = "1",
        xq: str = "1",
        kcdm: str = "",
        zc: str = "",
        electiveCourseForm_xkdetails: str = "",
        hidOption: str = "",
        xkh: str = "",
        kcmc: str = "",
        kcxf: str = "",
        kkxq: str = "",
        kcrkjs: str = "",
        skfs: str = "",
        xxyx: str = "",
        sksj: str = "",
        skdd: str = "",
        point_total: str = "100",
        point_used: str = "0",
        point_canused: str = "100",
        text_weight: str = "0",
        ck_gmjc: str = "on",
        ck_skbtj: str = "on"
    ):
        self.electiveCourseForm_xktype = electiveCourseForm_xktype
        self.electiveCourseForm_xn = electiveCourseForm_xn
        self.electiveCourseForm_xq = electiveCourseForm_xq
        self.electiveCourseForm_xh = electiveCourseForm_xh
        self.electiveCourseForm_nj = electiveCourseForm_nj
        self.electiveCourseForm_zydm = electiveCourseForm_zydm
        self.xqdm = xqdm
        self.electiveCourseForm_kcdm = electiveCourseForm_kcdm
        self.electiveCourseForm_kclb1 = electiveCourseForm_kclb1
        self.electiveCourseForm_kclb2 = electiveCourseForm_kclb2
        self.electiveCourseForm_khfs = electiveCourseForm_khfs
        self.electiveCourseForm_skbjdm = electiveCourseForm_skbjdm
        self.electiveCourseForm_xf = electiveCourseForm_xf
        self.electiveCourseForm_is_buy_book = electiveCourseForm_is_buy_book
        self.electiveCourseForm_is_cx = electiveCourseForm_is_cx
        self.electiveCourseForm_is_yxtj = electiveCourseForm_is_yxtj
        self.electiveCourseForm_xk_points = electiveCourseForm_xk_points
        self.xn = xn
        self.xn1 = xn1
        self._xq = _xq
        self.xq_m = xq_m
        self.xq = xq
        self.xh = xh
        self.kcdm = kcdm
        self.zc = zc
        self.electiveCourseForm_xkdetails = electiveCourseForm_xkdetails
        self.hidOption = hidOption
        self.xkh = xkh
        self.kcmc = kcmc
        self.kcxf = kcxf
        self.kkxq = kkxq
        self.kcrkjs = kcrkjs
        self.skfs = skfs
        self.xxyx = xxyx
        self.sksj = sksj
        self.skdd = skdd
        self.point_total = point_total
        self.point_used = point_used
        self.point_canused = point_canused
        self.text_weight = text_weight
        self.ck_gmjc = ck_gmjc
        self.ck_skbtj = ck_skbtj

    def __repr__(self):
        return f"TableFetcherParams({self.__dict__})"

    def to_dict(self):
        return self.__dict__

    def set_user_name(self, user_name):
        self.xh = user_name

class ScheduleFormat:
    def __init__(self, schedule_str):
        """
        :param schedule_str: 课程安排的字符串形式，如 '1-17周 三(5-7节)单'
        """
        self.weeks, self.day_of_week, self.start_period, self.end_period, self.is_odd_week = self._parse_schedule(
            schedule_str)

    def _parse_schedule(self, schedule_str):
        # 解析周次
        weeks = []
        week_pattern = r'(\d+(?:-\d+)?)(?![^(]*\))'
        weeks_match = re.findall(week_pattern, schedule_str)
        for week in weeks_match:
            weeks += self._parse_weeks(str(week))

        # 解析星期几
        day_of_week_match = re.search(r'([一二三四五六日])\(', schedule_str)
        day_of_week = day_of_week_match.group(1) if day_of_week_match else ''

        # 解析节次范围
        period_match = re.search(r'\((\d+)-(\d+)节\)', schedule_str)
        start_period = int(period_match.group(1)) if period_match else 0
        end_period = int(period_match.group(2)) if period_match else 0

        # 解析单双周
        is_odd_week = None
        if "单" in schedule_str:
            is_odd_week = "odd"
        elif "双" in schedule_str:
            is_odd_week = "even"

        return weeks, day_of_week, start_period, end_period, is_odd_week

    @staticmethod
    def _parse_weeks(weeks_str):
        if weeks_str == "":
            return list(range(1, 20))
        if '-' in weeks_str:
            start_week, end_week = map(int, weeks_str.split('-'))
        else:
            start_week, end_week = int(weeks_str), int(weeks_str)
        return list(range(start_week, end_week + 1))

    def conflicts_with(self, other):
        weeks_overlap = bool(set(self.weeks) & set(other.weeks))
        week_type_conflict = (self.is_odd_week == other.is_odd_week or
                              self.is_odd_week is None or other.is_odd_week is None)
        day_conflict = self.day_of_week == other.day_of_week
        period_conflict = not (self.end_period < other.start_period or self.start_period > other.end_period)
        return weeks_overlap and week_type_conflict and day_conflict and period_conflict

    def conflicts_with_list(self, other_list):
        for other in other_list:
            if self.conflicts_with(other):
                return True
        return False

    def __repr__(self):
        week_type = "单" if self.is_odd_week == "odd" else "双" if self.is_odd_week == "even" else "每"
        return f"周次: {self.weeks} 星期: {self.day_of_week} ({self.start_period}-{self.end_period}节) {week_type}周"

class Course:
    def __init__(
            self,
            selection_number=None,
            course_name=None,
            campus=None,
            teaching_method=None,
            instructor=None,
            start_week=None,
            credits=None,
            total_hours=None,
            limit=None,
            selected_count=None,
            confirmed_count=None,
            class_time=None,
            class_location=None,
            syllabus=None,
            teaching_calendar=None,
            notes=None
    ):
        """
        :param selection_number: 选课号
        :param course_name: 课程
        :param campus: 开课校区
        :param teaching_method: 授课方式
        :param instructor: 任课教师
        :param start_week: 起始周
        :param credits: 学分
        :param total_hours: 总学时
        :param limit: 限选人数
        :param selected_count: 已选人数
        :param confirmed_count: 确定人数
        :param class_time: 上课时间
        :param class_location: 上课地点
        :param syllabus: 教学大纲
        :param teaching_calendar: 教学日历
        :param notes: 备注
        """
        self.selection_number = selection_number
        self.course_name: str = course_name
        self.campus = campus

        self.teaching_method = teaching_method
        self.instructor = instructor

        self.start_week = start_week
        self.credits = credits
        self.total_hours = total_hours

        self.limit = limit
        self.selected_count = selected_count
        self.confirmed_count = confirmed_count

        self.class_time: list[ScheduleFormat] = []
        self.add_class_time(class_time)
        self.class_location = class_location

        self.syllabus = syllabus
        self.teaching_calendar = teaching_calendar
        self.notes = notes

    def __repr__(self):
        return (
            f"Course(selection_number='{self.selection_number}', course_name='{self.course_name}', campus='{self.campus}', "
            f"teaching_method='{self.teaching_method}', instructor='{self.instructor}', start_week='{self.start_week}', "
            f"credits={self.credits}, total_hours={self.total_hours}, limit={self.limit}, selected_count={self.selected_count}, "
            f"confirmed_count={self.confirmed_count}, class_time='{self.class_time}', class_location='{self.class_location}', "
            f"syllabus='{self.syllabus}', teaching_calendar='{self.teaching_calendar}', notes='{self.notes}')")

    def add_class_time(self, class_time):
        if class_time is not None:
            self.class_time.append(ScheduleFormat(class_time))

    def get_class_time_list(self):
        return self.class_time
