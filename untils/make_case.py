# encoding: utf-8

''' 根据Excel用例生成测试用例脚本 '''


import os
from untils.log_action import LOG

path = os.getcwd()


def read_header():
    path_header = path+'//case//compoment//case.txt'
    return open(path_header, encoding='utf-8').read()


def read_conten():
    path_conten = path+'//case//compoment//content.txt'
    return open(path_conten, encoding='utf-8').read()


def make_case_file(casename, desc, funtion_name):
    LOG.info("开始生成测试用例文件")
    file_path = path+'//case//script//'+casename+'_case.py'
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(read_header().format(casename, casename))
            file.write(read_conten().format(funtion_name, desc))
    else:
        pass


if __name__ == '__main__':
    casename, desc, funtion_name = ['reg', 'reg', 'reg']
    path_l = os.path.dirname(os.path.dirname(__file__))
    file_path = path_l + '//case//script//' + casename + '_case.py'
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            path_header = path_l + '//case//compoment//case.txt'
            path_conten = path_l + '//case//compoment//content.txt'
            file.write(open(path_header, encoding='utf-8').read().format(casename, casename))
            file.write(open(path_conten, encoding='utf-8').read().format(funtion_name, desc))
    else:
        pass