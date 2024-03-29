import pytest
import time
from base.Allure_Report import allure_generate
from base.SendEmail import send_mail
from conf import Conf
import os
report_path = Conf.report_path + os.sep + "result"
report_html = Conf.report_path + os.sep + "html"

if __name__ == '__main__':
    # 自定义参数
    # host="127.0.0.1",port="4723",bpport="4724",udid=None
    # --cmdopt 字典
    # 并发测试
    cmdopt = {"host": "10.86.80.95",
              "port": "4723",
              "bpport": "4724",
              "udid": "192.168.49.101:5555",
              "systemPort": 8208}
    pytest.main([f"--cmdopt={cmdopt}", "--alluredir", report_path])

    # pytest.main()
    # time.sleep(2)
    # allure_generate(report_path, report_html)
    # time.sleep(3)
    # send_mail(content="测试完成，请查看测试报告")

    # # 原版无Jenkins
    # cmdopt = {"host": "127.0.0.1",
    #           "port": "4723",
    #           "bpport": "4724",
    #           "udid": "192.168.49.101:5555"}
    # pytest.main([f"--cmdopt={cmdopt}"])
    # time.sleep(2)
    # allure_generate(report_path, report_html)
    # time.sleep(3)
    # send_mail(content="测试完成，请查看测试报告")

# 实现出错自动拍图，图片与allure合并显示
# 1、结果验证
# 2、断言失败拍图
# 3、图片与allure合并
