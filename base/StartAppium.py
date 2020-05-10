import socket
import subprocess
from utils.LogUtil import my_log
import platform
import re

log = my_log("start_appium")


# appium自动运行
# 1、检查端口号
# 用socket方式，连接上则端口号开启，反之没有开启
def check_port(host="127.0.0.1", port="4723"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # 连接
        s.connect((host, int(port)))
        s.shutdown(2)
        log.info('port %s is used!' % port)
        # print('port %s is used!' % port)
        return False
    except:
        log.info('port %s is not used' % port)
        # print('port %s is not used' % port)
        return True


# 2、启动
def appium_start(host="127.0.0.1", port="4723", bpport="4724", udid=None):
    # 1、判断端口号是否存在，存在不启动，不存在启动
    if check_port(host, port):
        pass
        # 2、定义启动参数
        cmd = "appium -a %s -p %s -bp %s -U %s --session-override" % (host, port, bpport, udid)
        # 3、subprocess.call，Popen
        appium_process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # 4、根据信息验证是否启动成功
        while True:
            line = str(appium_process.stdout.readline().strip(), "utf-8")
            log.info(line)
            if "usage" in line or "Error" in line:
                log.error("启动失败，出错信息为%s" % str(appium_process.stderr.readline().strip(), "utf-8"))
                break
            if "listener started" in line:
                log.info("启动成功：启动参数是：host为%s,port为%s,bpport为%s,udid为%s" % (host, port, bpport, udid))
                break


# # 3、停止
# def stop_server(port="4723"):
#     if not check_port():
#         # 1、判断系统环境，是windows还是mac
#         system_platform = platform.system()
#         # 2、根据系统环境，执行相应的命令
#         if system_platform.lower() == "windows":
#             cmd = "taskkill /f /im node.exe"
#         else:
#             cmd_lsof = "lsof -i:{0}|grep {0}".format(port)
#             cmd = cmd_lsof + "|awk '{print $2}'|xargs kill -9"
#             print(cmd)
#         subprocess.call(cmd, shell=True)
#     else:
#         log.info("该端口未运行")
#
#
# # 获取devices信息
# # 1、adb命令devices
# def get_devices():
#     cmd_adb = 'adb devices -l'
#     devices_info = subprocess.Popen(cmd_adb, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     # 2、信息获取udid
#     # print(devices_info.stdout.readlines())
#     devices_list = list()
#     for line in devices_info.stdout.readlines():
#         if "model" in str(line, encoding="utf-8"):
#             devices_list.append(str(line, encoding="utf-8"))
#     # re.search
#     get_devices_list = list()
#     for info in devices_list:
#         info = str(info)
#         udid = re.search(r'(.*?)device', info).group(1).strip()
#         get_devices_list.append(udid)
#     log.info("获取的devices信息udid:%s" % get_devices_list)
#     return get_devices_list


if __name__ == '__main__':
    # check_port()
    appium_start()
    # stop_server()
    # get_devices()
