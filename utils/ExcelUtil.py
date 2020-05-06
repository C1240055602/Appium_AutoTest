import os
import xlrd


# 自定义异常类
class SheetTypeError:
    pass


# 1、定义类
class ExcelReader:
    # 2、类初始化，读取文件，文件参数，文件验证
    def __init__(self, excel_file, sheet_by):
        # 假如文件存在，不存在报异常
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_by = sheet_by
            self._data = list()
        else:
            raise FileNotFoundError("文件不存在，请确认！")

    # 3、创建workbook
    def data(self):
        # 判断data存在不读取，不存在读取
        if not self._data:
            workbook = xlrd.open_workbook(self.excel_file)
            # 4、读取sheet，索引，名称
            # 判断sheet_by这个类型
            if type(self.sheet_by) not in [str, int]:
                raise SheetTypeError("请输入int or str类型")
            elif isinstance(self.sheet_by, int):
                sheet = workbook.sheet_by_index(self.sheet_by)
            elif isinstance(self.sheet_by, str):
                sheet = workbook.sheet_by_name(self.sheet_by)
            # 5、读取sheet里面数据
            # 数据返回List [字典，字典 ] [{},{}] 字典key:value 首行内容与每行测试数据组合
            # [{"序号":"1"，"描述":"登录功能测试"},{"序号":"2"，"描述":"注册测试"}]
            # 获取首行信息
            title = sheet.row_values(0)
            # 循环sheet数据，与首行组成dict，放在List
            # data = []
            for row in range(1, sheet.nrows):
                row_value = sheet.row_values(row)
                # 与首行组成字典，放在list
                self._data.append(dict(zip(title, row_value)))
        return self._data


# 6、执行


# head = ["序号","描述"]
# value1 = ["1","登录功能测试"]
# value2 = ["2","注册功能测试"]
# zip
# data_list = list()
# print(dict(zip(head,value1)))
# print(dict(zip(head,value2)))
# data_list.append(dict(zip(head,value1)))
# data_list.append(dict(zip(head,value2)))
# print(data_list)
if __name__ == '__main__':
    reader = ExcelReader("../excel_test/data.xls", "TestSteps")
    print(reader.data())
