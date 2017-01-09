from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest

class LoginTests(unittest.TestCase):
    baseurl = 'https://letskodeit.teachable.com'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseurl)

    lp = LoginPage(driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):

        self.lp.login('test@email.com','abc123abc')

        result=self.lp.verifyLoginFail()

        assert result == True

    @pytest.mark.run(order=2)
    def test_validLogin(self):

        self.lp.login('test@email.com','abcabc')

        result=self.lp.verifyLoginSucess()

        assert result == True

        self.driver.quit()


