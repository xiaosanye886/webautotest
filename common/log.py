#创建日志和错误截图保存的路径和文件名

import os
import time

err_img_path = ""

class Log:
        
    def mkdir_report(self):#创建一个日志文件，文件名随时间变化，防止别覆盖
        fl = os.getcwd() #获取当前运行文件的储存路径
        fl = "%s/log/report_%s" % (fl, time.strftime("%Y%m%d%H%M%S"))
        print(fl)
        if os.path.exists(fl):
            return None
        os.mkdir(fl)
        global err_img_path
        err_img_path = fl
        return fl

    def get_screenshot(self, driver, fl_name):#截图并保存在制定目录下
        err_img = "%s/%s" % (err_img_path, fl_name)
        driver.get_screenshot_as_file(err_img)
