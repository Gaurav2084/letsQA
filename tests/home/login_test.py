from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseurl='https://letskodeit.teachable.com'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseurl)

        lp=LoginPage(driver)
        lp.login('test@email.com','abcabc')

        result=lp.verifyLoginSucess()

        assert result == True





        driver.quit()


