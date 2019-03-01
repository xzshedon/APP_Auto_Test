# encoding: utf-8
''' 日志相关 '''

import os,logbook
from logbook.more import ColorizedStderrHandler
from functools import wraps


check_path = '.'
LOG_DIR = os.path.join(check_path, 'testlog')
file_stream = False
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    file_stream = True


# 官方提供的事例代码
def get_logger(name='appium', file_log=file_stream, level=''):
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    logbook.TimedRotatingFileHandler(
            os.path.join(LOG_DIR, '%s.log' % name),
            date_format='%Y%m%d%H', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)


LOG = get_logger(file_log=file_stream, level='INFO')


# TODO：研究其实现原理
def logger(param):
    def wrap(function):
        @wraps(function)
        def _wrap(*args, **kwargs):
            LOG.info("正在->{}".format(param))
            LOG.info("kwargs参数->{}".format(str(kwargs)))
            return function(*args, **kwargs)
        return _wrap
    return wrap
