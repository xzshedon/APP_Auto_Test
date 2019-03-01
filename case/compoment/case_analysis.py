# encoding: utf-8

''' 解析测试步骤，按照需求进行测试用例
   默认的定位的最后的一组为断言 '''

import time
from untils.get_yaml import open_yaml
from untils.log_action import LOG,logger
from untils.driver_base import DriverBase


@logger('解析测试步骤')
class CaseAnalysis():

    def __init__(self, driver, path):
        self.driver = driver
        self.path = path

    def open_file(self):
        return open_yaml(path=self.path)

    '''
    dict_items(
    [('id', 'login1'), ('model', '登录'), ('logout', 0.0), 
    ('case', {'phone': '13333333333', 'code': '123456', 'login': ''}), 
    ('assert', {'success': '0', 'assert': {'login': ''}})]
    )
    '''

    # 解析和控制操作步骤
    def exec_case(self, **kwargs):
        data = self.open_file()['data']
        driver = DriverBase(driver=self.driver)
        case_dir = kwargs.get('case')
        case_assert = kwargs.get('assert')

        if len(case_assert) <= 0:
            assert_result = {'code': 1, 'result':'fail', 'data': "请检查您的测试步骤最后一步断言是否填写"}  # code=1，断言无效
            return assert_result

        # 控件操作
        for case_key, case_value in case_dir.items():
            elem = self.elem_info(case_key, data)
            f = driver.find_elements(attr=elem['find_type'], tag=elem['element_info'])
            if f and len(f) > 0:
                if case_value == '':     # 若控件不带参数，执行click..等操作，TODO：增加更多控件操作
                    if elem['operate_type'] == 'click':
                        f[int(elem['index'])].click()
                else:
                    if elem['operate_type'] == 'send_key':
                        f[int(elem['index'])].clear()
                        f[int(elem['index'])].set_value(case_value)
                time.sleep(2)
            else:
                LOG.info('未找到控件:%s' % elem)
                assert_result = {'code': 0, 'result':'fail', 'data': "未找到控件->%s" % elem}   # code=0，断言有效
                return assert_result

        # 断言处理
        elem_key_list = list(case_assert['assert'].keys())
        elem_value_list = list(case_assert['assert'].values())
        if case_assert['success'] == "0":  # 不要找到断言控件
            for key in elem_key_list:
                elem_assert = self.elem_info(key, data)
                # 查找断言控件是否存在
                elem_list = driver.find_elements(attr=elem_assert['find_type'], tag=elem_assert['element_info'])
                if len(elem_list) == 0:
                    # 控件不存在,返回断言成功+断言信息
                    case_assert = {'code': 0, 'result': 'pass', 'data': "断言成功"}
                else:
                    # 控件存在,进一步判断控件属性,返回断言状态+断言信息
                    if elem_value_list[0] != '' and elem_list[0].text != elem_value_list[0]:
                        # 控件存在，但属性不同，返回成功
                        case_assert = {'code': 0, 'result': 'pass', 'data': "控件存在，但属性不一致，断言成功"}
                    else:
                        # 控件存在，属性为空或相同，返回失败
                        case_assert = {'code': 0, 'result': 'fail', 'data': "控件存在，断言失败"}
        else:  # 要找到断言控件
            for key in elem_key_list:
                elem_assert = self.elem_info(key, data)
                # 查找断言控件是否存在
                elem_list = driver.find_elements(attr=elem_assert['find_type'], tag=elem_assert['element_info'])
                if len(elem_list) == 0:
                    # 控件不存在,返回断言失败+断言信息
                    case_assert = {'code': 0, 'result': 'fail', 'data': "控件不存在，断言失败"}
                else:
                    # 控件存在,进一步判断属性是否相同,返回断言状态+断言信息
                    if elem_value_list[0] != '' and elem_list[0].text != elem_value_list[0]:
                        # 控件存在，但属性不同，返回失败
                        case_assert = {'code': 0, 'result': 'fail', 'data': "控件存在，但属性不一致，断言失败"}
                    else:
                        # 控件存在，属性为空或相同，返回成功
                        case_assert = {'code': 0, 'result': 'pass', 'data': "断言成功"}
        return case_assert

    # 在yaml data中找到与用例可以相同的控件
    def elem_info(self, key, data):
        for elem in data:
            if elem['key'] == key:
                return elem
            else:
                pass



