from selenium import webdriver
from time import sleep
from page.pagebase import PageBase

class LoginPage(PageBase):

    def open_page(self):#相当于重写父类PageBase里的open_page函数
        self.dr.get("http://localhost/agileone/index.php")
    
    def login_test(self, usr, pw):
        '''
        函数说明：不保存账号方式的登录
        参数说明：
            usr：账号名
            pw：密码值
        '''
        user_ele = ("id", "username")  # 账号输入框
        pw_ele = ("id", "password")  # 密码输入框
        save_ele = ("id", "savelogin")  # 保存账号的单选框
        login_ele = ("id", "login")  # 登录按钮

        self.open_page()
        first_t = self.get_title()#获取还未登录时页面的标题
        self.ele_send_keys(self.find_ele(user_ele[0], user_ele[1]), usr)
        sleep(1)
        self.ele_send_keys(self.find_ele(pw_ele[0], pw_ele[1]), pw)
        sleep(1)
        self.ele_click(self.find_ele(save_ele[0], save_ele[1]))
        sleep(1)
        self.ele_click(self.find_ele(login_ele[0], login_ele[1]))
        sleep(1)
        last_t = self.get_title()#获取登录后页面的标题
        return first_t, last_t

    def login_prompt(self):
        msg_ele = ("id", "msg")  # 提示信息元素

        msg_text = self.get_text(self.find_ele(msg_ele[0], msg_ele[1]))
        return msg_text

