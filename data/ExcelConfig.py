# 1、定义sheet名称类
class ExcelSheet:
    TEST_CASE = "TestCases"
    TEST_STEP = "TestSteps"
    TEST_DATA = "CaseData"
    TEST_ELEMENTS = "Elements"


# 2、每个sheet数据映射

# TestCases
class TestCases:
    # 序号	描述	TC_ID	是否运行	备注
    CASES_NUM = "序号"
    CASES_DESC = "描述"
    CASES_TC_ID = "TC_ID"
    CASES_IS_RUN = "是否运行"
    CASES_NOTE = "备注"


# steps
class TestSteps:
    # TC_ID	步骤ID	步骤名称	操作	元素名称	数据
    STEP_TC_ID = "TC_ID"
    STEP_ID = "步骤ID"
    STEP_NAME = "步骤名称"
    STEP_OPERATE = "操作"
    STEP_ELEMENT_NAME = "元素名称"
    STEP_DATA = "数据"


# CaseData
class CaseData:
    # C_ID	CASE_ID	是否运行	用例名称	测试数据	期望结果
    DATA_TC_ID = "TC_ID"
    DATA_CASE_ID = "CASE_ID"
    DATA_IS_RUN = "是否运行"
    DATA_NAME = "用例名称"
    DATA_INPUT = "测试数据"
    DATA_EXPECT_RESULT = "期望结果"


# ELEMENTS
# TC_ID	元素名称	定位类型	元素信息
class Elements:
    ELE_TC_ID = "TC_ID"
    ELE_NAME = "元素名称"
    ELE_BY = "定位类型"
    ELE_VALUE = "元素信息"
