#定义页面查找元素以及对查找到的元素进行的而相关操作
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class PageBase:

    def __init__(self):
        self.dr = webdriver.Chrome()

    def open_page(self):
        self.dr.get(url)

    def find_ele(self, locator, value):
        #lower()函数将大写字母转为小写字母
        if locator.lower() == "id":
            ele = self.dr.find_element_by_id(value)
        elif locator.lower() == "name":
            ele = self.dr.find_element_by_name(value)
        elif locator.lower() == "class_name":
            ele = self.dr.find_element_by_class_name(value)
        elif locator.lower() == "tag_name":
            ele = self.dr.find_element_by_tag_name(value)
        elif locator.lower() == "xpath":
            ele = self.dr.find_element_by_xpath(value)
        elif locator.lower() == "link_text":
            ele = self.dr.find_element_by_link_text(value)
        elif locator.lower() == "partial_link_text":
            ele = self.dr.find_element_by_partial_link_text(value)
        elif locator.lower() == "css_selector":
            ele = self.dr.find_element_by_css_selector(value)
        else:
            return None
        return ele

    def ele_click(self, click_ele):
        click_ele.click()

    def ele_send_keys(self, sk_ele, value):
        sk_ele.send_keys(value)

    def ele_double_click(self, d_ele):
        ActionChains(self.dr).double_click(d_ele).perform()

    def get_title(self):
        return self.dr.title

    def get_text(self, ele):
        return ele.text
        
    def page_close(self):
        self.dr.close()

    def page_quit(self):
        self.dr.quit()