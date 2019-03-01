# encoding: utf-8

''' case主体结构 '''

import ddt,os,time
from appium import webdriver
from untils.parameter import Parameter
from untils.get_case import get_case
from untils.log_action import LOG
from untils.merge_conf import make_dis
from untils.performance import get_cpu,get_ram
from untils.record_txt import write_record
from untils.result import save_result
from config.config import TestAppPackage
from case.compoment.case_init import CaseInit
from untils.get_phone_info import get_ime

path = os.getcwd()
test_case = path + '//case//testcase.xlsx'
# TODO: 传值控制excel sheet
data_test = get_case(test_case, index=0)


@ddt.ddt
class AutoCase(Parameter):
    def __init__(self, parm, methodName='runTest'):
        super(AutoCase, self).__init__(methodName)
        self.port = parm['port']
        LOG.info(parm)
        self.parm = parm

    def setUp(self):
        self.dis_app = make_dis(
            Testplatform=self.parm['platformName'],
            TestplatformVersion=self.parm['platformVersion'],
            Testdevicesname=self.parm['deviceName'],
            TestappPackage=self.parm['appPackage'],
            TestappActivity=self.parm['appActivity']
        )
        self.driver = webdriver.Remote('http://localhost:' + self.port + '/wd/hub', self.dis_app)
        LOG.info('开始执行测试用例')
        time.sleep(8)

    def tearDown(self):
        LOG.info('测试执行完毕，正在恢复测试环境！')
        get_ime(self.parm['deviceName'])
        time.sleep(10)
        self.driver.quit()

    @ddt.data(*data_test)
    def test_case(self, data_test):
        case = CaseInit(driver=self.driver)
        self.asserture = case.case_init(**data_test)
        cpu = get_cpu(package_name=TestAppPackage,device=self.parm['deviceName'])
        ram = get_ram(package_name=TestAppPackage,device=self.parm['deviceName'])
        write_record(cpu=cpu, ram=ram, device=str(self.parm['deviceName']))
        if self.asserture[0] == "pass":
            dut = self.parm['udid']
            data = str(dut) +'&'+'pass'+'&'+str(data_test)+'&'+str(self.asserture[1])
            save_result(data)
        else:
            dut = self.parm['udid']
            data = str(dut) +'&'+'fail'+'&'+str(data_test)+'&'+str(self.asserture[1])
            save_result(data)