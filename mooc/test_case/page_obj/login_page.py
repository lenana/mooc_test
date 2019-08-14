from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    url = 'user/newlogin/from_url/1020/'
    base_url = 'https://www.imooc.com/'
    mooc_login_user_loc = (By.XPATH, "//span[@class='xa-showSignup']")

    def mooc_login(self):
        self.find_element(*self.mooc_login_user_loc).click()

    login_username_loc = (By.NAME, "email")
    login_password_loc = (By.NAME, "password")
    login_button_loc = (By.XPATH, "//form[@id='signup-form']/div[5]/input")

    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def user_login(self,username="username",password="1111"):
        self.open()
        self.mooc_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    user_error_hint_loc = (By.XPATH, "//form[@id='signup-form']/div[1]/p")
    pawd_error_hint_loc = (By.XPATH, "//form[@id='signup-form']/div[2]/p")

    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text


