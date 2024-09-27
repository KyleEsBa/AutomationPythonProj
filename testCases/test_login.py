import time
import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage

class Test_Login:
    baseURL="http://admin-demo.nopcommerce.com/"
    username="admin@yourstore.com"
    password="admin"

    def test_homePageTitle(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title
        self.driver.close()
        if actual_title=="Your store. Login":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title=self.driver.title
        if actual_title=="Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
        self.lp.clickLogout()

    def test_Sample(self, setup):
        self.driver=setup
        self.driver.get('http://www.google.com/')
        time.sleep(2)
        search_box = self.driver.find_element('name','q')
        search_box.send_keys('ChromeDriver')
        search_box.submit()
        time.sleep(2)
        self.driver.close()
