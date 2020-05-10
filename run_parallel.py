import concurrent.futures
import pytest
from base.Allure_Report import allure_generate
from conf import Conf
import os


# 1.方法实现
def run_pytest(device):
    report_path = Conf.report_path + os.sep + "result" + os.sep + device["name"]
    report_html = Conf.report_path + os.sep + "html" + os.sep + device["name"]

    pytest.main([f"--cmdopt={device}", "--alluredir", report_path])
    # time.sleep(2)
    allure_generate(report_path, report_html)


# 3.pool并发
def run_pool(devices):
    with concurrent.futures.ProcessPoolExecutor(len(devices)) as executor:
        executor.map(run_pytest, devices)


if __name__ == '__main__':
    # 2.参数列表
    devices_list = list()
    device_1 = {"host": "127.0.0.1",
                "port": "4723",
                "bpport": "4724",
                "udid": "192.168.49.101:5555",
                "systemPort": 8200,
                "name": "华为mate9"}
# 192.168.56.104:5555   192.168.56.105:5555
    device_2 = {"host": "127.0.0.1",
                "port": "4725",
                "bpport": "4726",
                "udid": "192.168.49.102:5555",
                "systemPort": 8201,
                "name": "华为mate10"}
    devices_list.append(device_1)
    devices_list.append(device_2)
    run_pool(devices_list)

# 1、复制一下run.py代码
# 2、ProcessPoolExecutor并发
# 1.方法实现

# 2.参数列表
# 3.pool并发
