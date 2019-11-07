# !usr/bin/env python
# coding=utf-8

import unittest
import HTMLTestRunner
unittest.main
class BaiduTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start')

    @classmethod
    def tearDownClass(cls):
        print('stop')
    def test1(self):
        print('第一个用例')
    def test2(self):
        print('第二个用例')
        raise Exception('error')
    def test3(self):
        print('xiuxiu')

if __name__=='__main__':
    suite=unittest.TestSuite(unittest.makeSuite(BaiduTest))
    unittest.TextTestRunner(verbosity=2).run(suite)

