# encoding: utf-8

''' 采集的性能数据保存到txt文件中 '''

import os,time
from untils.log_action import LOG,logger
from config.config import current_time

path = os.getcwd()
record = path+'//testreport//%s//perf.txt' % current_time


@logger('记录当前的cpu占用率，内存')
def write_record(cpu, ram, device):
    try:
        with open(record,'a',encoding='utf-8') as f:
            m = '%s: CPU:%s, RAM:%s' % (device, cpu, ram)
            f.write(m+'\n')
            f.close()
    except Exception as e:
        LOG.info('写入性能数据失败！失败原因：%s' % e)
        