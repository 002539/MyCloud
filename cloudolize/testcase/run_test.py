__author__ = 'FangXin'
import sys,time
sys.path.append('./')
from HTMLTestRunner import HTMLTestRunner
import unittest

#指定测试用例为当下目录下的testcase
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='demo_api_test.py')

if __name__ == "__main__":

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = "F:\\PycharmDemo\\cloud\\cloudolize\\report\\" + now + "_result.html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp, title='云哟接口测试报告', description='报告如下所示：')
    runner.run(discover)
    fp.close()
