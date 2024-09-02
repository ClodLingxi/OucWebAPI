import urllib
from urllib.parse import quote, quote_from_bytes


class FetcherParams:

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
        self.sel_kc = sel_kc.encode('GB2312')
        self.kcmc = kcmc

    def __repr__(self):
        return (f"QueryParameters(initQry={self.initQry}, xktype={self.xktype}, xh='{self.xh}', "
                f"xn='{self.xn}', xq={self.xq}, nj='{self.nj}', zydm='{self.zydm}', "
                f"items='{self.items}', xnxq='{self.xnxq}', kcfw='{self.kcfw}', "
                f"sel_nj='{self.sel_nj}', sel_zydm='{self.sel_zydm}', sel_schoolarea='{self.sel_schoolarea}', "
                f"sel_cddwdm='{self.sel_cddwdm}', sel_kc='{self.sel_kc}', kcmc='{self.kcmc}')")

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
            "sel_kc": self.sel_kc,
            "kcmc": self.kcmc
        }


class Course:
    def __init__(self, selection_number, course_name, campus, teaching_method, instructor, start_week, credits,
                 total_hours, limit, selected_count, confirmed_count, class_time, class_location, syllabus,
                 teaching_calendar, notes):
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
        self.course_name = course_name
        self.campus = campus

        self.teaching_method = teaching_method
        self.instructor = instructor

        self.start_week = start_week
        self.credits = credits
        self.total_hours = total_hours

        self.limit = limit
        self.selected_count = selected_count
        self.confirmed_count = confirmed_count

        self.class_time = []
        self.class_time.append(class_time)
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
        self.class_time.append(class_time)
