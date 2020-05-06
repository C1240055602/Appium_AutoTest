"""
数据处理：获取运行测试用例列表，根据列表去执行测试内容、测试步骤、action
#1、初始化测试用例文档，分别初始化4个sheet对象
#2、分别定义读取4个sheet数据的方法
#3、获取全部真实有效的测试用例 方法
#4、根据tc_id获取相应的列表数据
#5、判断是否运行列  y,获取执行测试用例
#6、获取运行测试用例列表
"""
from utils.LogUtil import my_log
from utils.ExcelUtil import ExcelReader
from data.ExcelConfig import ExcelSheet
from data.ExcelConfig import TestCases, TestSteps, CaseData, Elements


# 初始化测试用例文档，分别初始化4个sheet对象
# 1、创建类，初始化测试用例文档

class Data:
    def __init__(self, case_file):
        self.log = my_log()
        # 2、分别实例化4个sheet对象
        # self.reader_cases = ExcelReader(case_file, "TestCases")
        # self.reader_data = ExcelReader(case_file, "CaseData")
        # self.reader_steps = ExcelReader(case_file, "TestSteps")
        # self.reader_elements = ExcelReader(case_file, "Elements")
        self.reader_cases = ExcelReader(case_file, ExcelSheet.TEST_CASE)
        self.reader_data = ExcelReader(case_file, ExcelSheet.TEST_DATA)
        self.reader_steps = ExcelReader(case_file, ExcelSheet.TEST_STEP)
        self.reader_elements = ExcelReader(case_file, ExcelSheet.TEST_ELEMENTS)

    # 分别定义读取4个sheet数据的方法
    # 1、reader_cases
    def get_cases_sheet(self):
        """
        获取测试用例testcases sheet的数据
        :return:
        """
        return self.reader_cases.data()

    # 2、reader_data
    def get_data_sheet(self):
        """
        获取测试用例数据case data sheet的数据
        :return:
        """
        return self.reader_data.data()

    # 3、reader_steps
    def get_steps_sheet(self):
        """
        获取测试步骤 sheet的数据
        :return:
        """
        return self.reader_steps.data()

    # 4、reader_elements
    def get_elements_sheet(self):
        """
        获取元素对象 sheet的数据
        :return:
        """
        return self.reader_elements.data()

    # 获取全部真实有效的测试用例 方法
    # 1、获取testcases 数据
    def get_cases_all(self):
        """
        获取全部测试用例，过滤空的内容
        :return:
        """
        # 按条件TC_ID从全部数据列表中过滤，获取非空数据
        data_list = self.get_cases_sheet()
        # res = []
        # for data in data_list:
        #     if data["TC_ID"] != "":
        #         res.append(data)
        res = self.get_no_empty(data_list, TestCases.CASES_TC_ID)
        return res

    # 2、获取测试数据data case
    def get_data_all(self):
        """
        获取全部测试用例，过滤空的内容
        :return:
        """
        # 按条件TC_ID从全部数据列表中过滤，获取非空数据
        data_list = self.get_data_sheet()
        # res = []
        # for data in data_list:
        #     if data["TC_ID"] != "":
        #         res.append(data)
        res = self.get_no_empty(data_list, CaseData.DATA_TC_ID)
        return res

    # 避免代码冗余写成get_no_empty方法
    def get_no_empty(self, data_list, condition):
        """
        按条件condition获取数据，过滤非空数据
        :param data_list:
        :param condition:
        :return:
        """
        res = []
        for data in data_list:
            if data[condition] != "":
                res.append(data)
        return res

    # 3、获取测试步骤 step
    def get_steps_all(self):
        """
        获取steps 有效全部数据
        :return:
        """
        data_list = self.get_steps_sheet()
        res = self.get_no_empty(data_list, TestSteps.STEP_TC_ID)
        return res

    # 4、获取元素elements
    def get_elements_all(self):
        """
        获取元素 全部数据
        :return:
        """
        data_list = self.get_elements_sheet()
        res = self.get_no_empty(data_list, Elements.ELE_TC_ID)
        return res

    # 根据tc_id获取相应的列表数据
    # 1、data
    def get_data_by_tc_id(self, tc_id):
        """
        根据tc_id来获取data数据
        :param tc_id:
        :return:
        """
        # 1、获取全部列表数据
        data_all = self.get_data_all()
        # 2、根据tc_id获取数据，列表
        # data_all_tc = []
        # for data in data_all:
        #     if data["TC_ID"] == tc_id:
        #         data_all_tc.append(data)
        data_all_tc = self.get_by_tc_id(data_all, tc_id)
        return data_all_tc

    # 避免代码冗余写成get_no_empty方法
    def get_by_tc_id(self, data_list, tc_id):
        """
        根据tc_id来获取数据，新的列表
        :param data_list:
        :param tc_id:
        :return:
        """
        data_all_tc = []
        for data in data_list:
            if data["TC_ID"] == tc_id:
                data_all_tc.append(data)
        return data_all_tc

    # 2、step
    def get_steps_by_tc_id(self, tc_id):
        """
        根据tc_id来获取steps数据
        :param tc_id:
        :return:
        """
        # 1、获取全部列表数据
        data_all = self.get_steps_all()
        data_all_tc = self.get_by_tc_id(data_all, tc_id)
        return data_all_tc

    # 3、element
    def get_elements_by_tc_id(self, tc_id):
        """
        根据tc_id来获取elements数据
        :param tc_id:
        :return:
        """
        # 1、获取全部列表数据
        data_all = self.get_elements_all()
        data_all_tc = self.get_by_tc_id(data_all, tc_id)
        return data_all_tc

    def get_elements_by_element(self, tc_id, element_name):
        """
        根据步骤sheet中的元素名称和tc_id 获取相应的数据
        :param tc_id:
        :param element_name:
        :return:
        """
        elements = self.get_elements_by_tc_id(tc_id)
        res = None
        for ele in elements:
            if str(ele[Elements.ELE_NAME]) == str(element_name):
                res = ele
        return res

    # 判断是否运行列  y,获取执行测试用例
    # 1、testcase
    def get_run_cases(self):
        """
        按条件是否运行，y,获取case执行测试用例
        :return:
        """
        # 根据是否运行 == y/Y,获取执行测试用例
        # 获取全部测试
        run_list = self.get_cases_all()
        run_cases_list = []
        # 对应列 "是否运行" ==y/Y,生成新的执行测试用例
        for line in run_list:
            if str(line[TestCases.CASES_IS_RUN]).lower() == "y":
                run_cases_list.append(line)
        return run_cases_list

    # 2、casedata
    def get_run_data(self, tc_id):
        """
        按条件是否运行，y,获取data执行测试用例
        :return:
        """
        # 根据是否运行 == y/Y,获取执行测试用例
        # 获取全部测试
        run_list = self.get_data_all()
        run_cases_list = []
        # 对应列 "是否运行" ==y/Y,生成新的执行测试用例
        for line in run_list:
            if str(line[CaseData.DATA_IS_RUN]).lower() == "y" and tc_id in line[CaseData.DATA_TC_ID]:
                run_cases_list.append(line)
        return run_cases_list

    # 获取运行测试用例列表
    def run_list(self):
        # 1、获取testcase执行测试用例列表
        cases = self.get_run_cases()
        self.log.debug("获取TestCases表测试个数{}，数据内容{}".format(len(cases), cases))
        # 2、根据这个列表中的tc_id来获取对应data数据
        data_list = list()
        for case in cases:
            tc_id = case[CaseData.DATA_TC_ID]
            # tmp_data_list = self.get_run_data(tc_id)
            # desc = case[TestCases.CASES_DESC]
            # note = case[TestCases.CASES_NOTE]
            # for data in tmp_data_list:
            #     # 1、增加备注
            #     data.update({TestCases.CASES_NOTE: note})
            #     # 2、增加描述
            #     data.update({TestCases.CASES_DESC: desc})

            data_list.extend(self.get_run_data(tc_id))
            # data_list.append(self.get_run_data(tc_id))
        self.log.debug("获取CaseData运行测试个数{}，数据内容{}".format(len(data_list), data_list))
        return data_list


#
#     def ttt(self):
#         a = [{"a": "1", "b": "2"}, {"a": "3", "b": "4"}]
#         b = {"描述": "登录"}
#         c = {"备注": "登录测试"}
#         # b.update(c)
#         # print(b)
#         # print(c)
#         print("添加之前a", a)
#         for i in a:
#             print(i)
#             i.update(b)
#             i.update(c)
#         print("添加之后a", a)


if __name__ == '__main__':
    res_data = Data("../data/data.xls")
    # print(res_data.get_cases_all())
    print(res_data.get_data_all())
    # print(res_data.get_steps_all())
    # print(res_data.get_elements_all())
    print(res_data.get_data_by_tc_id("TC_Login"))
    print(res_data.get_steps_by_tc_id("TC_Login"))
    print(res_data.get_run_cases())
    print(res_data.get_run_data("TC_Login"))
    print(res_data.run_list())
