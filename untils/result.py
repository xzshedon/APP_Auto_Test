# encoding: utf-8

''' 保存测试结果 '''

import os,time
from untils.log_action import LOG,logger
from config.config import current_time

path = os.getcwd()
result = path + '//testreport//%s//log.txt' % current_time
# result = '/Users/a/Desktop/appium_test//testreport//20190228182809//log.txt'


@logger('保存测试结果')
def save_result(data):
    if os.path.exists(result) is True:
        with open(result, 'a',encoding='utf-8') as f:
            f.write(data+'\n')
            f.close()
    else:
        f = open(result, 'a')
        f.write(data+'\n')
        f.close()
    LOG.info('记录测试结果完毕')


@logger('解析测试结果')
def parse_result(device):
    with open(result, 'r+', encoding='utf-8') as f:
        res = f.readlines()
    list_result = []
    for j in res:
        if device in j:
            list_result.append({'device': device,
                                'result': j.split('&')[1],
                                'parameter': j.split('&')[2],
                                'reason': j.split('&')[-1]})
    pass_num = 0
    fail_num = 0
    for i in list_result:
        if i['result'] == 'pass':
            pass_num += 1
        else:
            fail_num += 1
    LOG.info('解析测试结果完成')
    return pass_num, fail_num, list_result


if __name__ == '__main__':
    device_t = 'e811deb7'
    pass_num, fail_num, list_result = parse_result(device_t)
    print(pass_num, fail_num)
    for each in list_result:
        print(each)