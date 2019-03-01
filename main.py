# encoding: utf-8

''' 主运行文件 '''

import os
import unittest,random,datetime
from untils.report_excel import create
from untils.log_action import LOG,logger
from untils.make_case import make_case_file
from untils.parameter import Parameter
from untils.appium_server import AppiumServer
from untils.get_apk_info import AndroidDebugBridge
from untils.get_phone_info import get_phone_info
from multiprocessing import Pool
from case.script.reg_case import AutoCase
from config.config import current_time
from config.config import Test_version


devices_list = []
file_path = os.getcwd()
report_path = file_path + "//testreport//%s" % current_time
if not os.path.exists(report_path):
    os.makedirs(report_path)


@logger('生成设备配置链接的进程池')
def runner_pool(getDevices):
    '''
        根据链接的设备生成不同的dict
        然后放到设备的list里面
        设备list的长度产生进程池大小
    '''
    devices_pool = []
    for i in range(0, len(getDevices)):
        _pool = []
        _initApp = {}
        _initApp["deviceName"] = getDevices[i]["devices"]
        _initApp["udid"] = getDevices[i]["devices"]
        _initApp["platformVersion"] = get_phone_info(device=_initApp["deviceName"])["release"]
        _initApp["platformName"] = "android"
        _initApp["port"] = getDevices[i]["port"]
        _initApp["appPackage"] = 'com.kaihei.baobao'
        _initApp["appActivity"] = '.core.welcome.WelcomeActivity'
        _pool.append(_initApp)
        devices_pool.append(_initApp)
    pool = Pool(len(devices_pool))
    pool.map(runner_case_app, devices_pool)
    pool.close()
    pool.join()


@logger('组织测试用例')
def runner_case_app(devices):
    '''利用unittest的testsuite来组织测试用例'''
    test_suit = unittest.TestSuite()
    test_suit.addTest(Parameter().parametrize(AutoCase, param=devices))
    unittest.TextTestRunner(verbosity=2).run(test_suit)


if __name__ == '__main__':
    LOG.info("开始执行测试")
    start_time = datetime.datetime.now()
    devices = AndroidDebugBridge().attached_devices()
    make_case_file('reg', 'reg', 'reg')
    path = os.getcwd()
    file_name = path + '//testreport//%s//' % current_time + 'result.xlsx'
    if not os.path.exists(file_name):
        f = open(file_name,'w')
        f.close()
    if len(devices)>0:
        for dev in devices:
            app = {}
            app["devices"] = dev
            app["port"] = str(random.randint(4593, 4698))
            devices_list.append(app)
        appium_server = AppiumServer(devices_list)
        appium_server.start_server()
        runner_pool(devices_list)
        try:
            appium_server.stop_server(devices_list)
        except Exception as e:
            LOG.info("关闭appium服务失败，原因：%s" % e)
        end_time = datetime.datetime.now()
        hour = end_time - start_time
        create(file_name=file_name, test_time=str(hour), test_version=Test_version, devices_list=devices)
        LOG.info("测试执行完毕，耗时：%s" % hour)
    else:
        LOG.info("未找到设备")
        print("没有可用设备")