# encoding: utf-8

''' 性能数据采集 '''


from untils.log_action import logger
import platform, os


def get_sys_filter():
    '''根据所运行的系统获取adb不一样的筛选条件'''
    system = platform.system()
    if system == 'Windows':
        find_manage = 'findstr'
    else:
        find_manage = 'grep'
    return find_manage

find = get_sys_filter()


@logger('采集cpu信息')
def get_cpu(package_name, device):
    '''这里采集的cpu时候可以是执行操作采集 就是-n  -d  刷新间隔'''
    try:
        cmd = 'adb -s %s shell top -n 1 | %s %s' % (device, find, package_name)
        re_cpu = os.popen(cmd).read().split()[2]
        return re_cpu
    except:
        pass


@logger('获取使用的物理内存信息')
def get_ram(package_name, device):
    '''Total 的实际使用过物理内存'''
    try:
        cmd = 'adb -s %s shell top -n 1| %s %s' % (device,find, package_name)
        re_ram = os.popen(cmd).read().split()[6]
        re_ram_m = str(round(int(re_ram[:-1])/1024)) + 'M'
        return re_ram_m
    except:
        pass