import subprocess

from utils.LogUtil import my_log

log = my_log("allure_generate")


# 1、allure_cmd命令
def allure_generate(report_path, report_html):
    allure_cmd = "allure generate %s -o %s --clean" % (report_path, report_html)
    # 2、subprocess.call
    log.info("报告地址%s", report_path)
    try:
        subprocess.call(allure_cmd, shell=True)
        log.info("报告地址%s", report_html)
    except Exception as e:
        log.error("生成测试报告失败，请检查配置")
        raise e
