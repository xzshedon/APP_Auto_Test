# encoding: utf-8

''' unittest的参数封装 '''

import unittest


class Parameter(unittest.TestCase):

    def __int__(self, methodName="runTest", parme=None):
        super(Parameter, self). __init__(methodName)
        self.parme = parme

    def parametrize(self, test_case, param=None):
        test_loader = unittest.TestLoader()
        test_name = test_loader.getTestCaseNames(test_case)
        suite = unittest.TestSuite()
        for name in test_name:
            suite.addTest(test_case(methodName=name, parm=param))
        return suite
