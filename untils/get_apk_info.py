# encoding: utf-8

''' APK相关信息获取 '''

import re, subprocess, os
from untils.log_action import LOG


class ApkInfo():

    def __init__(self, apkPath):
        self.apkPath = apkPath

    # 获得APP包名、appkey、版本
    def get_apk_base_info(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        if not match:
            raise Exception("can't get packageinfo")
        packagename = match.group(1)
        appKey = match.group(2)
        appVersion = match.group(3)
        LOG.info("=====getApkInfo=========")
        LOG.info('packageName:', packagename)
        LOG.info('appKey:', appKey)
        LOG.info('appVersion:', appVersion)
        return packagename, appKey, appVersion

    # 得到启动类
    def get_launch_activity(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("launchable-activity: name=(\S+)").search(output.decode())
        if match is not None:
            return match.group(1)

    # 得到应用的名字
    def get_apk_name(self):
        cmd = "aapt dump badging " + self.apkPath + " | grep application-label: "
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[0].decode()[19:-1]
        return result


class AndroidDebugBridge(object):
    def call_adb(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        results = os.popen(command_text, "r")
        while 1:
            line = results.readlines()
            if not line: break
            command_result += line
        results.close()
        return command_result

    # 拉去数据到本地
    def pull(self, remote, local):
        result = self.call_adb("pull %s %s" % (remote, local))
        return result

    # 获取链接的设备
    def attached_devices(self):
        devices = []
        result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE).stdout.readlines()
        for item in result:
            t = item.decode().split("\tdevice")
            if len(t) >= 2:
                devices.append(t[0])
        return devices


if __name__ == '__main__':
    devices = AndroidDebugBridge().attached_devices()
    print(devices)