from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_logger as cl

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        SeleniumDriver.__init__(self,driver)
        self.driver=driver

    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = 'commit'

    # def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_button)

    def clickLoginLink(self):
        self.elementClick(self._login_link,locatorType='link')

    def enterEmail(self,email):
        self.sendkeys(email,self._email_field)

    def enterPassword(self,password):
        self.sendkeys(password,self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button,locatorType='name')

    def login(self,email,password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSucess(self):
        elementPresent= self.isElementPresent('//span[text()="User Settings"]',locatorType='xpath')
        return elementPresent

    def verifyLoginFail(self):
        pass
