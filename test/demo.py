# import unittest,ddt,os,time
# from appium import webdriver
# from untils.log_action import LOG
# from untils.merge_conf import make_dis
# from untils.get_case import get_case
# from untils.performance import get_cpu,get_ram
# from untils.record_txt import write_record
# from untils.result import save_result
# from config.config import TestAppPackage
# from case.compoment.case_init import CaseInit
# from main import devices_list
#
#
# path = os.getcwd()
# test_case = path+'\\case\\testcase.xlsx'
# data_test = get_case(test_case, index=1)
#
# @ddt.ddt
# class AutoTest(unittest.TestCase):
#
#     def __init__(self, parm, method_name='run_test'):
#         super(AutoTest, self).__init__(method_name)
#         self.port = parm['port']
#         print(parm)
#
#     def setup(self):
#         self.dis_app = make_dis(Testplatform=self.parm['platformName'],
#                                 TestplatformVersion=self.parm['platformVersion'],
#                                 Testdevicesname=self.parm['deviceName'],
#                                 TestappPackage=self.parm['appPackage'],
#                                 TestappActivity=self.parm['appActivity'])
#         self.driver = webdriver.Remote('http://localhost:' + self.port + '/wd/hub', self.dis_app)
#         LOG.info('开始执行测试用例')
#
#     def tearDown(self):
#         LOG.info('测试执行完毕，正在恢复测试环境！')
#         time.sleep(15)
#         self.driver.quit()
#
#
#     @ddt.data(*data_test)
#     def test(self, data_test):
#         case = CaseInit(driver=self.driver)
#         self.asserture = case.case_init(**data_test)
#         cpu = get_cpu(TestAppPackage)
#         ram = get_ram(TestAppPackage)
#         write_record(cpu=cpu, ram=ram)
#         self.assertEqual(data_test['assert'], self.asserture,
#                          mag='fail resons: %s != %s' % (data_test['assert', self.asserture]))
#



























# encoding: utf-8

import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p : os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


# demo运行，需要现在控制台：appium &

class BaoBaoAndroidTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = 'e811deb7'
        desired_caps['appPackage'] = 'com.kaihei.baobao'
        desired_caps['appActivity'] = '.core.welcome.WelcomeActivity'
        desired_caps['noReset'] = True
        desired_caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(8)

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    def test_add(self):
        self.driver.find_elements_by_id('com.kaihei.baobao:id/tab_tv_label')[1].click()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BaoBaoAndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

