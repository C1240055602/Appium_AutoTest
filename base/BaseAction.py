from utils.LogUtil import my_log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import allure
import datetime


# 1、定义类
class Action:
    def __init__(self, driver):
        self.driver = driver
        self.log = my_log("Base_Page")

    # 2、定义方法

    # 元素定位
    # byid,byxpath
    # 元素等待方法
    # 1、click
    # 2、send_keys
    # 3、toast

    # click  id,xpath
    def by_xpath(self, value):
        """
        xpath 元素定位
        :param value:
        :return:
        """
        return self.by_find_element(By.XPATH, value)

    def by_id(self, value):
        """
        id 元素定位
        :return:
        """
        return self.by_find_element(By.ID, value)

    # send_keys
    def send_keys(self, **kwargs):
        """
        通过id定位元素，发送内容
        :param by:
        :param value:
        :param send_value:
        :return:
        """
        # self.by_find_element(By.ID, value).send_keys(send_value)
        by, value = kwargs["by"], kwargs["value"]
        if by == "id":
            loc = self.by_id(value)
        elif by == "xpath":
            loc = self.by_xpath(value)
        loc.click()
        loc.send_keys(kwargs["send"])

    # WebDriverWait
    def by_find_element(self, by, value, timeout=30, poll=3):
        """
        隐式等待，寻找元素
        :param by:
        :param value:
        :param timeout:
        :param poll:
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))
            return self.driver.find_element(by, value)
        except Exception as e:
            self.log.error("没有找到该元素：{}".format(e))

    # toast
    def is_toast_exist(self, **kwargs):
        # 1、使用by_find_element寻找元素，类型xpath，value自定义
        # 2、webdriverwait获取信息，text
        # toast_loc = "//*[contains(@text,'手机号格式错误')]"
        try:
            text = kwargs["expect"]
            toast_loc = "//*[contains(@text,'" + text + "')]"
            ele = WebDriverWait(self.driver, timeout=3, poll_frequency=0.5).until(
                lambda x: x.find_element(By.XPATH, toast_loc))
            self.log.info("获取toast内容为：{}".format(ele.text))
            return True
        except Exception as e:
            self.log.error("toast获取失败，错误信息：{}".format(e))
            return False

    def click_btn(self, **kwargs):
        # 根据by类型，进行by_id,by_xpath方法调用
        by, value = kwargs["by"], kwargs["value"]
        if by == "id":
            loc = self.by_id(value)
        elif by == "xpath":
            loc = self.by_xpath(value)

        loc.click()

    def assert_toast_result(self, **kwargs):
        toast_result = self.is_toast_exist(**kwargs)
        assert toast_result
        # try:
        #     assert toast_result == False
        # except Exception as e:
        #     png = self.driver.get_screenshot_as_png()
        #     allure.attach(png,"toast错误",allure.attachment_type.PNG)
        #     raise e


# 定义装饰器
# 1、定义装饰2层函数
def screenshot_allure(func):
    def get_err_screenshot(self, *args, **kwargs):
        # 2、定义内部函数，拍图操作
        try:
            func(self, *args, **kwargs)
        except Exception as e:
            png = self.driver.get_screenshot_as_png()
            name = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            allure.attach(png, name, allure.attachment_type.PNG)
            raise e

    # 3、返回内部函数名称
    return get_err_screenshot
# 4、重构toast断言
# 5、调用装饰器@


# # 元素滑动
# def swipeUp(self, t=500, n=1):
#     """向上滑动屏幕"""
#     screen = self.get_window_size()
#     x1 = screen['width'] * 0.5  # x坐标
#     y1 = screen['height'] * 0.75  # 起始y坐标
#     y2 = screen['height'] * 0.25  # 终点y坐标
#     for i in range(n):
#         self.swipe(x1, y1, x1, y2, t)
#
# def swipeDown(self, t=500, n=1):
#     """向下滑动屏幕"""
#     screen = self.get_window_size()
#     x1 = screen['width'] * 0.5  # x坐标
#     y1 = screen['height'] * 0.25  # 起始y坐标
#     y2 = screen['height'] * 0.75  # 终点y坐标
#     for i in range(n):
#         self.swipe(x1, y1, x1, y2, t)
#
# def swipLeft(self, t=500, n=1):
#     """向左滑动屏幕"""
#     screen = self.get_window_size()
#     x1 = screen['width'] * 0.75
#     y1 = screen['height'] * 0.5
#     x2 = screen['width'] * 0.25
#     for i in range(n):
#         self.swipe(x1, y1, x2, y1, t)
#
# def swipRight(self, t=500, n=1):
#     """向右滑动屏幕"""
#     screen = self.get_window_size()
#     x1 = screen['width'] * 0.25
#     y1 = screen['height'] * 0.5
#     x2 = screen['width'] * 0.75
#     for i in range(n):
#         self.swipe(x1, y1, x2, y1, t)
#
# def get_window_size(self, screen):
#     return screen
