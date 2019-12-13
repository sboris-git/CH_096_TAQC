from Tests.test_main import TestInit
from Pages.LoginPage import LoginPage
from Driver.driver import browser_setup


class Test_Login(TestInit):

    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()
        self.driver.get(browser_setup["url"])

    # def test_login_if_user_entered(self):
    #     self.login_Page = LoginPage(self.driver)
    #     self.login_Page.click_on_login_button()
    #     self.login_Page.type_login(TestData.LOGIN_USER)
    #     self.login_Page.type_pass(TestData.PASSWORD_USER)
    #     self.login_Page.press_button_signin()

    def test(self):
        self.login_Page = LoginPage(self.driver)
        self.login_Page.login()