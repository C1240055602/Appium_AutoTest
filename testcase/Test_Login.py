import unittest
from conf import Caps
from pages.Page_Main import BxgMainPage
from pages.Page_Login import BxgLoginPages
import time


# 1、PO模式+unittest，导入包，继承unittest.TestCase
class Login(unittest.TestCase):
    # 2、定义测试用例方法,test_login
    def test_login(self):
        # list
        driver = Caps.desired_caps()  # 初始化
        bxgmain = BxgMainPage(driver)
        bxglogin = BxgLoginPages(driver)
        # 3、编写测试用例步骤
        # 登录测试用例
        # 1.点击暂不需要按钮
        bxgmain.allow_click()
        time.sleep(2)
        # 2.点击我的
        bxgmain.me_click()
        # 3.输入用户名
        bxglogin.username_send("13133")  # 特殊字符，汉字
        # 4.输入验证码
        bxglogin.code_send("131")
        # 5.点击登录
        bxglogin.login_click()
        # 6.获取toast
        toast = bxglogin.toast()
        print(toast)

    def test_login_2(self):
        driver = Caps.desired_caps()
        bxgmain = BxgMainPage(driver)
        bxglogin = BxgLoginPages(driver)
        # 3、编写测试用例步骤
        # 登录测试用例
        # 1.点击暂不需要按钮
        bxgmain.allow_click()
        time.sleep(2)
        # 2.点击我的
        bxgmain.me_click()
        # 3.输入用户名
        bxglogin.username_send("@#$%^&*()")  # 特殊字符，汉字
        # 4.输入验证码
        bxglogin.code_send("131")
        # 5.点击登录
        bxglogin.login_click()
        # 6.获取toast
        toast = bxglogin.toast()
        print(toast)
# 4、运行
