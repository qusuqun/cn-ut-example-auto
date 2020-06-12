import sys
sys.path.append(r'D:\selenium_python\Python\cn-ut-example-auto')
from common.calculator import Count
import unittest

class TestCount(unittest.TestCase):
    # 测试的初始化
    def setUp(self):
        print("test start")

    #测试用例add的编写
    def test_add(self):
        self.Count = Count(2, 3)
        self.assertEqual(self.Count.add(), 5)

    # 测试用例sub的编写
    def test_sub(self):
        self.Count = Count(6, 3)
        self.assertEqual(self.Count.sub(), 3)

    # 测试用例mul的编写
    def test_mul(self):
        self.Count = Count(6, 3)
        self.assertEqual(self.Count.mul(), 18)

    # 测试用例div的编写
    def test_div(self):
        self.Count = Count(6, 3)
        self.assertEqual(self.Count.div(), 2)

    # 测试的回收-测试的环境还原
    def tearDown(self):
        print("test end")

