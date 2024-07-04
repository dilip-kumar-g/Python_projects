
from selenium import webdriver
import unittest
from Unittest_framework_2.Data.methods import TestMethods as tm
from Unittest_framework_2.Utilities import Utilities as lc
from Unittest_framework_2.Utilities.Utilities import LoginLocators as vl


class LoginPageTest(unittest.TestCase):

    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def tearDown(cls):
        cls.driver.quit()


    def test_TC_login_03(self):
        result = tm.forgot_password_link(self.driver)
        self.assertEqual(result,"Reset Password link sent successfully")


    def test_TC_PIM_03(self):
        self.driver.get(lc.login_url)
        tm.login_to_OragneHRM_stat(self.driver,vl.valid_username, vl.valid_password)
        value = tm.title_verification(self.driver)
        result = tm.validation_on_admin_page(self.driver)
        self.assertEqual(value,"OrangeHRM")
        self.assertEqual(result,lc.side_panel)


    def test_TC_PIM_04(self):
        self.driver.get(lc.login_url)
        tm.login_to_OragneHRM_stat(self.driver, vl.valid_username, vl.valid_password)
        result = tm.validate_main_menu(self.driver)
        self.assertEqual(result,lc.main_menu)


if __name__ == "__main__":
    unittest.main()





