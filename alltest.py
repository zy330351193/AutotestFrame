# !usr/bin/env python
# coding=utf-8
import unittest
import os
import time
import HTMLTestRunner

def alltest():
    suite = unittest.defaultTestLoader.discover(start_dir=os.path.join(os.path.dirname(__file__), 'testcase'),
                                                pattern='test_*.py',top_level_dir=None)
    return suite
def getnowtime():
    return time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))
def run():
    filename=os.path.join(os.path.dirname(__file__),'report',getnowtime()+'report.html')
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='自动化测试报告',description='报告详细信息')
    runner.run(alltest())
if __name__=='__main__':
    run()
