# encoding: utf-8

''' 获取配置文件相关的app配置信息 '''

from config.config import *
from untils.log_action import logger


@logger('开始从配置文件中获取测试相关的配置')
def make_dis(Testplatform, TestplatformVersion, Testdevicesname, TestappPackage, TestappActivity):
    dis_app = {'platformName': Testplatform,
               'platformVersion': TestplatformVersion,
               'deviceName': Testdevicesname,
               'appPackage': TestappPackage,
               'appActivity': TestappActivity,
               'androidDeviceReadyTimeout': TestAndroidDevicereadyTimeout,
               'unicodeKeyboard': TestUnicodeKeyboard,  # 使用unicode输入法
               'resetkeyboard': TestResetKeyboard,  # 重置输入法到初始状态
               'noSign': TestNOSign,  # 不需要再次签名
               'noReset': TestNoReset,  # 启动app时不要清除app里的原有的数据
               'automationName': 'uiautomator2'
               }
    return dis_app
