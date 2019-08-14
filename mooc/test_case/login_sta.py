from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from .models import myunit, screenshot
from .page_obj.login_page import login

class loginTest(myunit.MyTest):
    '''社区登录测试'''
    def user_login_verify(self,username="",password=""):
        login(self.driver).user_login(username,password)

    def test_login1(self):
        '''用户名，密码为空登录'''
        self.user_login_verify()
        po=login(self.driver)
        self.assertEqual(po.user_error_hint(),"账号不能为空")
        self.assertEqual(po.pawd_error_hint(),"密码不能为空")
        screenshot.insert_img(self.driver,"user_pawd_empty.jpg")

    def test_login2(self):
        '''用户名正确，密码为空登录'''
        self.user_login_verify(username="pytest")
        po=login(self.driver)
        self.assertEqual(po.pawd_error_hint(),"密码不能为空")
        screenshot.insert_img(self.driver,"pawd_empty.jpg")

    def test_login3(self):
        '''用户名为空，密码正确'''
        self.user_login_verify(password="abc123")
        po=login(self.driver)
        self.assertEqual(po.user_error_hint(),"账号不能为空")
        screenshot.insert_img(self.driver,"user_empty.jpg")

    def test_login4(self):
        '''用户名密码不匹配'''
        character = random.choice('sdhdjhsjdjk')
        username = "zhangsan"+character
        self.user_login_verify(username=username,password="123456")
        po=login(self.driver)
        self.assertEqual(po.pawd_error_hint(),"账户名密码不匹配")
        screenshot.insert_img(self.driver,"user_pawd_error.jpg")

    def test_login5(self):
        '''用户名密码正确'''
        self.user_login_verify(username="zhangsan",password="12345")
        sleep(2)
        po=login(self.driver)
        self.assertNotEqual(po.user_error_hint(),"账号不能为空")
        self.assertNotEqual(po.pawd_error_hint(),"密码不能为空")
        screenshot.insert_img(self.driver,"user_pawd_ture.jpg")

if __name__=="__main__":
    unittest.main()
