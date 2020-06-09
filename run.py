import unittest
from HTMLTestRunner import HTMLTestRunner
from common.log import Log
from time import strftime

log = Log()
#确定report路径，以及report文件名
fl_path = log.mkdir_report()
fl_name = "%s/report_%s.html" % (fl_path, strftime("%Y%m%d%H%M%S"))

#创建测试集
suite = unittest.defaultTestLoader.discover("./testcase", pattern="test*.py")

#运行测试集
fl = open(fl_name, mode="wb")
runner = HTMLTestRunner(stream=fl, title="Agileone测试报告", description="功能测试")
runner.run(suite)
