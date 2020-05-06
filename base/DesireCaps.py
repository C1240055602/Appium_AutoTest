# encoding:utf8
from utils.YamlUtil import YamlReader
from conf import Conf
from appium import webdriver

# 1、通过yaml来读取caps.yml
reader = YamlReader(Conf.conf_caps)
data = reader.data()


# 2、结果，字典转换

def appium_desired_caps():
    # 2、desired创建字典
    desired_caps = dict()
    # 3、platformName
    desired_caps['platformName'] = data['platformName']
    # 4、platformVersion
    desired_caps['platformVersion'] = data['platformVersion']
    # 5、deviceName
    desired_caps['deviceName'] = data['deviceName']
    # 6、启动程序的包名appPackage
    desired_caps["appPackage"] = data['appPackage']
    # 7、启动界面名appActivity
    desired_caps['appActivity'] = data['appActivity']
    # 解决中文
    desired_caps["unicodeKeyboard"] = data['unicodeKeyboard']
    desired_caps["resetKeyboard"] = data['resetKeyboard']

    # 获取toast automationName = uiautomator2
    desired_caps["automationName"] = data['automationName']

    # 8、http，连接appium服务器
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    driver.implicitly_wait(20)

    return driver
