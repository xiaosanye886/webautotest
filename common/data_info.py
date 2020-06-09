import csv

class CsvInfo:
    """进行Csv格式文件操作"""

    def get_info(self, fl):
    #定义一个函数读取csv文件里的数据，csv表格每一行数据作为一个列表元素插入列表info_list
        info_list = []

        '''
        csv_fl = open(fl)
        content = csv.reader(csv_fl)
        csv_fl.close()
        for i in content:
            info_list.append(i)
        if not info_list:
            print("%s文件为空" % fl)
            raise Exception
        return info_list
        
        '''
        with open(fl) as csv_fl:
            content = csv.reader(csv_fl)
            for i in content:
                info_list.append(i)
            if not info_list:
                print("%s文件为空" % fl)
                raise Exception
        return info_list

    def get_login_info(self):
    #上一个函数获得的列表元素里包含不需要的说明列，这个函数把需要的测试数据（用户名和密码）
    #从上一个列表中遍历出来，方便读取使用
        login_info = []

        info_lst = self.get_info("./data/login.csv")
        for (i, j) in enumerate(info_lst):
            if i == 0:
                continue
            tmp_list = [j[2], j[3]]
            login_info.append(tmp_list)
        print(login_info)
        return login_info

if __name__ == '__main__':
    c = CsvInfo()
    c.get_login_info()