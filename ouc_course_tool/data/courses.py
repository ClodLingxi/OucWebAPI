class FetcherParams:
    def __init__(self, initQry, xktype, xh, xn, xq, nj, zydm, items, xnxq, kcfw,
                 sel_nj, sel_zydm, sel_schoolarea, sel_cddwdm, sel_kc, kcmc):
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
        self.sel_kc = sel_kc
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
    def __init__(self, selection_number, course_name, campus, teaching_method, instructor, start_week, credits, total_hours, limit, selected_count, confirmed_count, class_time, class_location, syllabus, teaching_calendar, notes):
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
        return (f"Course(selection_number='{self.selection_number}', course_name='{self.course_name}', campus='{self.campus}', "
                f"teaching_method='{self.teaching_method}', instructor='{self.instructor}', start_week='{self.start_week}', "
                f"credits={self.credits}, total_hours={self.total_hours}, limit={self.limit}, selected_count={self.selected_count}, "
                f"confirmed_count={self.confirmed_count}, class_time='{self.class_time}', class_location='{self.class_location}', "
                f"syllabus='{self.syllabus}', teaching_calendar='{self.teaching_calendar}', notes='{self.notes}')")

    def add_class_time(self, class_time):
        self.class_time.append(class_time)
