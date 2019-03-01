# encoding: utf-8

''' 获取excel中的用例 '''

import xlrd
from untils.log_action import logger,LOG


@logger('获取测试用例所需要的参数')
def get_case(filepath, index):
    try:
        file = xlrd.open_workbook(filepath)
        sheet_case = file.sheets()[index]
        n_rows = sheet_case.nrows
        listdata = []
        for i in range(1, n_rows):
            dict_case = {}
            dict_case['id'] = sheet_case.cell(i, 0).value
            dict_case['model'] = sheet_case.cell(i, 1).value
            dict_case['logout'] = (sheet_case.cell(i, 2).value)
            dict_case['case'] = eval(sheet_case.cell(i, 3).value)
            dict_case['assert'] = eval(sheet_case.cell(i, 4).value)
            # dict_case.update(eval(sheet_case.cell(i, 3).value))
            # dict_case.update(eval(sheet_case.cell(i, 4).value))
            listdata.append(dict_case)
        return listdata
    except Exception as e:
        LOG.info('获取测试用例失败！原因：%s' % e)
        return e


if __name__ == '__main__':
    test_case = '/Users/a/Desktop/appium_test//case//testcase.xlsx'
    data_test = get_case(test_case, index=0)
    print(data_test)