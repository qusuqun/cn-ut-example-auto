import sys
sys.path.append(r'D:\selenium_python\Python\cn-ut-example-auto')
from src.test_method import TestCount
import os
import time
import unittest
import HTMLTestRunner

# 方法一：
pro_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(pro_dir, "src")
print(path)
discover = unittest.defaultTestLoader.discover(path, pattern="test*.py", top_level_dir=None)
print(discover)
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(discover)

# 方法二：
suite = unittest.makeSuite(TestCount, "test")
all_test = unittest.TestSuite(suite)
runner = unittest.TextTestRunner()
runner.run(all_test)


# 方法三：
suite = unittest.makeSuite(TestCount, "test")
runner = unittest.TextTestRunner()
runner.run(suite)

# 方法四：
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add"))
    suite.addTest(TestCount("test_sub"))
    suite.addTest(TestCount("test_mul"))
    suite.addTest(TestCount("test_div"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

# 方法五：
now = time.strftime("%Y%m%d_%H%M%S")
pro_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
report_name = now + " " + "testReport.html"
report_path = os.path.join(pro_dir, "testresult", report_name)
outfile = open(report_path, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='test report',
                                               description='calculator test report')
suite = unittest.makeSuite(TestCount, "test")
runner.run(suite)
outfile.close()