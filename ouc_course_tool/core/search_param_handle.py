from ouc_course_tool import CourseFetcherParams

def search_param_handle(course_list: list[str], campus, year_and_term):
    select_params_list = []
    for target in course_list:
        params = CourseFetcherParams(sel_schoolarea=campus, xnxq=year_and_term)
        if target.endswith('公共'):
            params.kcfw = 'PublicBasic'
            temp = target.split('-')
            params.set_keyword(temp[0])
        elif target.endswith('选修'):
            params.kcfw = 'Common'
            temp = target.split('-')
            params.set_keyword(temp[0])
        else:
            temp = target.split('-')
            if len(temp) == 3:
                if temp[1] == '智能科学':
                    params.set_keyword(temp[0])
                    params.sel_zydm = "0150"
                    params.sel_nj = temp[2]
        select_params_list.append(params.to_dict())
    return select_params_list