# encoding: utf-8

''' 手机相关信息获取 '''


import os
import subprocess


# 得到手机信息
def get_phone_info(device):
    cmd = "adb -s " + device + " shell cat /system/build.prop"
    phone_info = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  shell=True).stdout.readlines()
    release = "ro.build.version.release="  # 版本
    model = "ro.product.model="  # 型号
    brand = "ro.product.brand="  # 品牌
    device = "ro.product.device="  # 设备名
    result = {"release": release, "model": model, "brand": brand, "device": device}
    for line in phone_info:
        for i in line.split():
            temp = i.decode()
            if temp.find(release) >= 0:
                result["release"] = temp[len(release):]
                break
            if temp.find(model) >= 0:
                result["model"] = temp[len(model):]
                break
            if temp.find(brand) >= 0:
                result["brand"] = temp[len(brand):]
                break
            if temp.find(device) >= 0:
                result["device"] = temp[len(device):]
                break
    return result


# 得到最大运行内存
def get_meminfo(device):
    cmd = "adb -s "+device+" shell cat /proc/meminfo"
    get_cmd = os.popen(cmd).readlines()
    men_total = 0
    men_total_str = "MemTotal"
    for line in get_cmd:
        if line.find(men_total_str) >= 0:
            men_total = line[len(men_total_str)+1:].replace("kB", "").strip()
            break
    return int(men_total)


# 得到几核cpu
def get_cpu(device):
    cmd = "adb -s "+device+" shell cat /proc/cpuinfo"
    get_cmd = os.popen(cmd).readlines()
    find_str = "processor"
    int_cpu = 0
    for line in get_cmd:
        if line.find(find_str) >= 0:
            int_cpu += 1
    return str(int_cpu)+"核"


# 得到手机分辨率
def get_pix(device):
    result = os.popen("adb -s "+device+" shell wm size", "r")
    return result.readline().split("Physical size:")[1].strip()


def get_ime(device):
    # 获得手机中安装的输入法,并设置输入法
    result = os.popen("adb -s "+device+" shell ime list -s", "r")
    imes = result.readlines()
    tag_ime = [ime.replace("\n", '') for ime in imes if 'sogou' in ime or 'baidu' in ime]
    if len(tag_ime) > 0:
        cmd = 'adb -s %s shell ime set %s' % (device, tag_ime[0])
        os.system(cmd)
    else:
        os.system('adb -s shell ime set com.android.inputmethod.latin/.LatinIME' % device)


if __name__ == '__main__':
    # print(get_phone_info("e811deb7"))
    # print(get_cpu("e811deb7"))
    # print(get_meminfo("e811deb7"))
    # print(get_pix("e811deb7"))
    get_ime("e811deb7")
