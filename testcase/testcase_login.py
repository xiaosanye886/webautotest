import unittest#测试框架模块
from time import strftime#获取时间，为日志和截图命名
import common.log
from common.data_info import CsvInfo#读取测试数据
from page.loginpage import LoginPage #继承于父类PageBase，获取页面元素，并对页面元素进行操作
from common.log import Log#创建日志和错误截图保存的路径和文件名

#testcase001
class LoginTestCase(unittest.TestCase):#继承于unittest的类
    """登录页面测试用例"""

    def setUp(self):
        print("testcase001 start")
        self.login_ob = LoginPage()#创建一个对象变量
        self.log = Log()

    def testcase_001(self):
        c = CsvInfo()
        info_lst = c.get_login_info()#调用get_login_info函数读取csv文件里的测试数据（用户名和密码组成的列表）
        usr_name = info_lst[0][0]#获取第0个元素用户名
        pw = info_lst[0][1]#获取第1个元素密码
        first_t, last_t = self.login_ob.login_test(usr_name, pw)#通过self.login_ob对象调用loginpage里的login_test方法获取返回的登录前后的页面标题
        try:
            self.assertNOTEqual(first_t, last_t, msg="未登录成功")
        except:
            err_img = "testcase001_%s.png" % strftime("%Y%m%d%H%M%S")#定义截图保存的路径和名称
            self.log.get_screenshot(self.login_ob.dr, err_img)#通过self.log对象调用log里面的get_screenshot方法截图
            #raise AssertionError

    def tearDown(self):
        self.login_ob.page_close()#关闭网页

if __name__ == "__main__":
    unittest.main()
'''
#testcase002
try:
    print("testcase002 start")
    login_t, first_t = login("su", "admin1234")
    if login_t != first_t:
        print("testcase002 fail")
    else:
        print("testcase002 succ")
    text = login_fun.login_prompt()
    if "密码输入错误" not in text:
        print("testcase002 fail")
    else:
        print("")
    print("testcase002 end")
except:
    print("testcase002 fail")
    log.log_add()
finally:
    login_fun.ag_quit()

#testcase003
try:
    print("testcase003 start")
    login_t, first_t = login("admin1234", "admin")
    if login_t != first_t:
        print("testcase003 fail")
    else:
        print("testcase003 succ")
    text = login_fun.login_prompt()
    if "找不到该用户名" not in text:
        print("testcase003 fail")
    else:
        print("")
    print("testcase003 end")
except:
    print("testcase003 fail")
    log_add()
finally:
    login_fun.ag_quit()
'''