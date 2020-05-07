import unittest
from base.ExcelData import Data
from data.ExcelConfig import TestSteps, Elements, CaseData
from base.BaseAction import Action
from base.DesireCaps import appium_desired_caps
import time
from utils.LogUtil import my_log
from conf import Conf
from utils.YamlUtil import YamlReader

# 单个用例编写及运行
# 1、编写excel测试用例，4个sheet编写，并且执行1条测试用例 是否运行y
# 2、编写unittest测试用例
# 2.1 创建类，继续unittest
log = my_log("operate")


class Operate(unittest.TestCase):
    # setupclass
    @classmethod
    def setUpClass(cls):
        cls.driver = appium_desired_caps()
        pass

    # 2.2 测试用例，执行步骤，先不运行appium，打印excel流，流程确认
    def setUp(self):
        self.driver.launch_app()
        # pass

    # 获取可执行测试用例
    @unittest.skip("不运行")
    def test_step(self):
        data = Data("../data/data.xls")
        run_list = data.run_list()
        print(run_list)
        print(run_list[0][0])
        # 根据测试用例执行步骤
        # 1、根据tc_id获取步骤列表
        run_case = run_list[0][0]
        tc_id = run_case[TestSteps.STEP_TC_ID]
        steps = data.get_steps_by_tc_id(tc_id)
        # 2、循环步骤列表，一步一步执行
        for step in steps:
            print("执行步骤{}".format(step))
            # 2.3 执行appium，完成整体流程；setup tear
            # 1.click
            operate = step[TestSteps.STEP_OPERATE]
            elements = step[TestSteps.STEP_ELEMENT_NAME]
            element = data.get_elements_by_element(step[TestSteps.STEP_TC_ID], elements)
            print(element)
            by = element[Elements.ELE_BY]
            value = element[Elements.ELE_VALUE]
            if operate == "click":
                # elements = step[TestSteps.STEP_ELEMENT_NAME]
                # element = data.get_elements_by_element(step[TestSteps.STEP_TC_ID],elements)
                # print(element)
                # by = element[Elements.ELE_BY]
                # value = element[Elements.ELE_VALUE]
                Action(self.driver).click_btn(by, value)
                # pass
            # 2.text
            elif operate == "text":
                # 1、获取by,value,send_value内容
                send_value = step[TestSteps.STEP_DATA]
                # 2、send_value内容转换，通过case data数据内容
                data_input = run_case[CaseData.DATA_INPUT]
                print(data_input)
                # 3、字符串转换成字典
                # 1.通过,分割得到username=13718418220 password=123456
                res = {}
                # 2.通过=分割
                for i in str(data_input).split(","):
                    c = i.split("=")
                    res[c[0]] = c[1]
                # print(res)
                # 4、send_value内容获取最后结果send
                send = res[send_value]
                # print(send)
                # 5、send_keys发送
                Action(self.driver).send_keys(by, value, send)
            # 3.toast
            elif operate == "verify_toast":
                # 1.使用get_toast获取toast具体信息
                # text,case data期望结果
                text = run_case[CaseData.DATA_EXPECT_RESULT]
                # 调用方法获取toast
                toast = Action(self.driver).is_toast_exist(text)
                print(toast)
                # 2.toast结果进行验证
                # self.assertIn(text,toast)
                self.assertTrue(toast)
        time.sleep(2)

    def tearDown(self):
        self.driver.close_app()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 2.4 测试用例实现，根据步骤，具体操作 去映射关键字方法，执行操作
    # 多个用例，参数化运行

    # 需求：根据传入操作名称，自动去BaseAction类寻找对应方法，执行
    # 1、Excel操作步骤与关键字方法一个映射
    # 1. 创建yml文件
    # 2. Excel与方法映射
    # 3. 读取配置文件，根据key获取关键字方法
    # 2、关键字方法去baseaction类寻找方法，getattr内置函数
    # getattr(Action(self.driver),操作方法)
    # 1. 根据excel操作步骤映射获取字符串格式的方法名称
    # 2. 判断操作方法存不存在，存在，不存在不往下执行
    # 3. 根据字符串格式方法名称，getattr去获取对应的函数对象
    # 3、方法执行，参数重新调整
    # 1.click by ,value
    # 2.text  by ,value, send
    # 3.toast DATA_EXPECT_RESULT
    # 使用**kwargs 不定数量的关键字参数 key=value
    # 1. 创建字典，存放参数
    # 2. 调整方法，关键字方法，参数**kw
    # 3. 调用actionmethod方式去执行
    # 4、调试运行
    def get_keyword(self, name):
        # 1、读取配置文件，文件路径：绝对路径
        keyword_file = Conf.keywords_path
        # 2、YamlReader，data()
        reader = YamlReader(keyword_file).data()
        # 3、key获取值 name
        value = reader[name]
        return value

    def str_to_dict(self, content):
        # 3、字符串转换成字典
        # 1.通过,分割得到username=13718418220 password=123456
        res = {}
        # 2.通过=分割
        for i in str(content).split(","):
            c = i.split("=")
            res[c[0]] = c[1]
        return res

    def test_step_new(self):
        data = Data("../data/data.xls")
        run_list = data.run_list()
        run_case = run_list[0][0]
        tc_id = run_case[TestSteps.STEP_TC_ID]
        steps = data.get_steps_by_tc_id(tc_id)
        for step in steps:
            log.debug("执行步骤{}".format(step))
            # 获取元素信息
            elements = step[TestSteps.STEP_ELEMENT_NAME]
            element = data.get_elements_by_element(step[TestSteps.STEP_TC_ID], elements)
            log.debug("元素信息{}".format(element))
            # 操作步骤 关键表映射 click_btn
            operate = self.get_keyword(step[TestSteps.STEP_OPERATE])

            # 操作判断，是否存在，不存在不执行步骤
            if operate:
                # 定义方法参数：字典
                param_value = dict()

                # 根据getattr判断执行哪个方法
                action_method = getattr(Action(self.driver), operate)
                log.debug("该关键字是{}".format(operate))

                # 定义具体的参数
                by = element[Elements.ELE_BY]
                value = element[Elements.ELE_VALUE]
                # 1、获取by,value,send_value内容
                send_value = step[TestSteps.STEP_DATA]
                # 2、send_value内容转换，通过case data数据内容

                expect = run_case[CaseData.DATA_EXPECT_RESULT]
                param_value["by"] = by
                param_value["value"] = value

                param_value["expect"] = expect
                # 判断假如有输入内容 字符转换
                if send_value:
                    data_input = run_case[CaseData.DATA_INPUT]
                    send = self.str_to_dict(data_input)
                    param_value["send"] = send[send_value]

                action_method(**param_value)

            else:
                log.error("没有operate信息：{}".format(operate))
