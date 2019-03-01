# encoding: utf-8

''' 初始化测试用例 '''


import os
from untils.log_action import LOG,logger
from case.compoment.case_analysis import CaseAnalysis

path = os.getcwd()
ele_path = path + '//case//elements.yaml'


@logger('初始化测试用例')
class CaseInit:

    def __init__(self, driver):
        self.driver = driver
        self.path = ele_path
        self.open = CaseAnalysis(self.driver, path=self.path)

    def case_init(self, **kwargs):
        f = self.open.exec_case(**kwargs)
        if f['code'] == 1:
            LOG.info('无法获取断言')
            return ['fail', '断言格式有误，或无法获取断言']
        else:
            return [f['result'], f['data']]

