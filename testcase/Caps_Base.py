# encoding:utf8
from base.BaseAction import Action
from base.DesireCaps import appium_desired_caps
import time


# 1、创建类，继承Action
class CapsTest(Action):
    # 2、初始化webdriver
    def __init__(self):
        driver = appium_desired_caps()
        super().__init__(driver)

    # 3、登录这个方法，使用封装click,send_keys
    def login_test(self):

        self.click_btn("id", "com.boxuegu:id/negative_button")

        # 1、点击我的 id、class、xpath
        me = '//*[starts-with(@text,"我的")]'
        self.click_btn("xpath", me)
        time.sleep(5)
        # 2、输入用户名
        username = "com.boxuegu:id/edit_usr"
        self.send_keys("id", username, 13133)
        time.sleep(2)
        # 3、输入验证码
        code = "com.boxuegu:id/security_code"
        self.send_keys("id", code, 131)
        time.sleep(2)
        # 4、点击登录
        login_btn = "com.boxuegu:id/btn_login"
        self.click_btn("id", login_btn)
        # 5、获取toast信息
        toast = self.get_toast('手机号格式错误')
        print(toast)


# 4、运行
if __name__ == "__main__":
    cap_test = CapsTest()
    cap_test.login_test()
