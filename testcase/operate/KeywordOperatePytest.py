# encoding:utf8
import unittest
from base.ExcelData import Data
from data.ExcelConfig import TestSteps, Elements, CaseData, TestCases
from base.BaseAction import Action, screenshot_allure
from base.DesireCaps import appium_desired_caps
import ddt
from utils.LogUtil import my_log
from conf import Conf
from utils.YamlUtil import YamlReader
import allure

"""
1、重构，代码整理
2、pytest测试用例编写，新建测试文件
3、pytest框架用例执行，run.py，pytest.ini
4、运行及调试
"""

#
log = my_log("operate")

data = Data(Conf.testcase_file)
# #执行测试用例列表
run_list = data.run_list()


class Operate():
    # 加一个参数，获取初始化
    def __init__(self, driver):
        self.driver = driver

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

    def test_run(self, run_case):
        log.info("执行用例内容:{}".format(run_case))
        self.step(run_case)

    # pytest原版
    # def step(self, data, run_case):
    #     tc_id = run_case[TestSteps.STEP_TC_ID]
    #     # 获取步骤
    #     steps = data.get_steps_by_tc_id(tc_id)
    #     for step in steps:
    #         log.debug("执行步骤{}".format(step))
    #         # 获取元素信息
    #         elements = step[TestSteps.STEP_ELEMENT_NAME]
    #         element = data.get_elements_by_element(step[TestSteps.STEP_TC_ID], elements)
    #         log.debug("元素信息{}".format(element))
    #         # 操作步骤 关键表映射 click_btn
    #         operate = self.get_keyword(step[TestSteps.STEP_OPERATE])
    #
    #         # 操作判断，是否存在，不存在不执行步骤
    #         if operate:
    #             # 定义方法参数：字典
    #             param_value = dict()
    #
    #             # 根据getattr判断执行哪个方法
    #             action_method = getattr(Action(self.driver), operate)
    #             log.debug("该关键字是{}".format(operate))
    #
    #             # 定义具体的参数
    #             by = element[Elements.ELE_BY]
    #             value = element[Elements.ELE_VALUE]
    #             # 1、获取by,value,send_value内容
    #             send_value = step[TestSteps.STEP_DATA]
    #             # 2、send_value内容转换，通过case data数据内容
    #
    #             expect = run_case[CaseData.DATA_EXPECT_RESULT]
    #             param_value["by"] = by
    #             param_value["value"] = value
    #
    #             param_value["expect"] = expect
    #             # 判断假如有输入内容 字符转换
    #             if send_value:
    #                 data_input = run_case[CaseData.DATA_INPUT]
    #                 send = self.str_to_dict(data_input)
    #                 param_value["send"] = send[send_value]
    #
    #             action_method(**param_value)
    #
    #         else:
    #             log.error("没有operate信息：{}".format(operate))

    # allure美化
    @screenshot_allure
    def step(self, data, run_case):
        tc_id = run_case[TestSteps.STEP_TC_ID]
        # 获取步骤
        steps = data.get_steps_by_tc_id(tc_id)
        # allure报告
        # feature
        allure.dynamic.feature(run_case[TestCases.CASES_NOTE])
        # story
        allure.dynamic.story(run_case[TestCases.CASES_DESC])
        # title
        allure.dynamic.title(run_case[CaseData.DATA_CASE_ID] + "-" + run_case[CaseData.DATA_NAME])

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
                # step 步骤名称
                with allure.step(step[TestSteps.STEP_NAME]):
                    action_method(**param_value)

            else:
                log.error("没有operate信息：{}".format(operate))

# allure定制测试报告
# 1、testcases 备注 feature
# 2、testcases 描述 story
# 3、casedata case_id+用例名称  title
# 4、teststeps 步骤名称 step
