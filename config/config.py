# encoding: utf-8

''' 配置app以及测试设备的相关信息 '''

import time

TestAppPackage = 'com.kaihei.baobao'  # 被测应用包名
TestAndroidDevicereadyTimeout = 30  # 等待app启动的超时时间
TestUnicodeKeyboard = True
TestResetKeyboard = True
TestNOSign = True
TestNoReset = True
Test_Project_name = 'BaoBao'
TiTestuser = '幸子帅'
Test_user = '自动化'
Test_version = '1.4.0'

JAVA_HOME = '/Library/Java/JavaVirtualMachines/jdk-11.0.1.jdk/Contents/Home'
ANDROID_HOME = '/Users/a/Library/Android/sdk'

current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))