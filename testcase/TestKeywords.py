import pytest
from utils.LogUtil import my_log
from conf import Conf
from base.ExcelData import Data
from testcase.operate.KeywordOperatePytest import Operate
from base.DesireCaps import appium_desired_caps

log = my_log("TestKeywords")
data = Data(Conf.testcase_file)
# 执行测试用例列表
run_list = data.run_list()


# 1、创建测试用例方法
class TestKeyword:

    # @pytest.mark.parametrize("run_case", run_list)
    # def test_run(self, run_case):
    #     log.info("执行用例内容:{}".format(run_case))
    #     Operate(self.driver).step(data, run_case)
    #
    # def setup_class(self):
    #     self.driver = appium_desired_caps()
    #
    # def setup(self):
    #     self.driver.launch_app()
    #
    # # 2、重构代码
    #
    # # 3、增加setup teardown
    #
    # def teardown(self):
    #     self.driver.close_app()
    #
    # def teardown_class(self):
    #     self.driver.quit()

    # 原方式改成conftest参数运行
    @pytest.mark.parametrize("run_case", run_list)
    def test_run(self, start_appium_desired, run_case):
        self.driver = start_appium_desired
        self.driver.launch_app()
        log.info("执行用例内容:{}".format(run_case))
        Operate(self.driver).step(data, run_case)

    def teardown(self):
        self.driver.close_app()

    def teardown_class(self):
        self.driver.quit()
