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


# demo运行，需要先在控制台：appium &

class BaoBaoAndroidTest(unittest.TestCase):
    def setUp(self):
        d1_caps = {}
        d1_caps['platformName'] = 'Android'
        d1_caps['platformVersion'] = '7.1.2'
        d1_caps['deviceName'] = 'e811deb7'
        d1_caps['appPackage'] = 'com.kaihei.baobao'
        d1_caps['appActivity'] = '.core.welcome.WelcomeActivity'
        d1_caps['noReset'] = True
        d1_caps['automationName'] = 'uiautomator2'
        self.driver1 = webdriver.Remote('http://127.0.0.1:4723/wd/hub', d1_caps)  # 暴鸡
        d2_caps = {}
        d2_caps['platformName'] = 'Android'
        d2_caps['platformVersion'] = '5.1'
        d2_caps['deviceName'] = 'S4NZ8LCIY5LNE6WS'
        d2_caps['appPackage'] = 'com.kaihei.baobao'
        d2_caps['appActivity'] = '.core.welcome.WelcomeActivity'
        d2_caps['noReset'] = True
        d2_caps['automationName'] = 'uiautomator2'
        self.driver2 = webdriver.Remote('http://127.0.0.1:4723/wd/hub', d2_caps)  # 老板
        sleep(8)

    def tearDown(self):
        self.driver1.close_app()
        self.driver1.quit()
        self.driver2.close_app()
        self.driver2.quit()

    # 测试用户评价
    def test_user_evaluation(self):
        # 点击我的
        self.driver1.find_elements_by_id('com.kaihei.baobao:id/tab_tv_label')[1].click()
        sleep(1)
        # 点击个人主页
        self.driver1.find_element_by_id('com.kaihei.baobao:id/iv_edit').click()
        sleep(2)
        # 向上滑动
        self.driver1.swipe(0.5,0.8,0.5,0.2, duration=200)
        # 点击用户印象
        self.driver1.find_element_by_id('com.kaihei.baobao:id/tv_to_more_label').click()
        sleep(2)
        # 点击下拉菜单
        self.driver1.find_element_by_id('com.kaihei.baobao:id/iv_label_arrow').click()
        sleep(1)

    # 测试车队上车
    def test_car_board(self):
        # 暴鸡：点击车队
        self.driver1.find_elements_by_id('com.kaihei.baobao:id/tab_tv_label')[0].click()
        sleep(2)
        # 暴鸡：点击创建车队
        self.driver1.find_element_by_id('com.kaihei.baobao:id/img_fleet_create').click()
        sleep(2)
        # 暴鸡：点击确定创建
        self.driver1.find_element_by_id('com.kaihei.baobao:id/fleet_game_free_create').click()
        sleep(2)
        # 老板：点击车队
        self.driver2.find_elements_by_id('com.kaihei.baobao:id/item_game_name')[0].click()
        sleep(2)
        # 老板：选择白银段位
        self.driver2.find_element_by_name('秩序白银').click()
        sleep(1)
        # 老板：点击开始匹配
        self.driver2.find_element_by_id('com.kaihei.baobao:id/fleet_game_free_times').click()
        sleep(5)

        assert_boss = self.driver1.find_element_by_name('哟不错呦')
        boss = False
        if assert_boss:
            boss = True
        assert_leader = self.driver2.find_element_by_name('sunny12')
        leader = False
        if assert_leader:
            leader = True

        self.assertTrue(boss, '暴鸡，没有找打老板')
        self.assertTrue(leader, '老板，没有找到暴鸡')


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BaoBaoAndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

