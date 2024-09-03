from ouc_course_tool import FetcherParams

def search_param_handle(course_list: list[str], campus, year_and_term):
    select_params_list = []
    for target in course_list:
        params = FetcherParams(sel_schoolarea=campus, xnxq=year_and_term)
        if target.endswith('公共'):
            params.kcfw = 'PublicBasic'
            temp = target.split('-')
            params.set_sel_kc(temp[0])
        else:
            temp = target.split('-')
            if len(temp) == 3:
                if temp[1] == '智能科学':
                    params.set_sel_kc(temp[0])
                    params.sel_zydm = "0150"
                    params.sel_nj = temp[2]
        select_params_list.append(params.to_dict())
    return select_params_list