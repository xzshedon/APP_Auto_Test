# encoding: utf-8

''' 解析yaml中元素定位信息 '''

import yaml
from untils.log_action import LOG,logger


@logger('解析yaml文件')
def open_yaml(path):
    try:
        file = open(r'%s'%path, 'r', encoding='utf-8')
        data = yaml.load(file)
        return {'code':0, 'data':data}
    except Exception as e:
        LOG.info('yaml文件解析失败！原因：%s' % e)
        return {'code':1, 'data':e}

