import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Capstone_2.Pages.login import ValidationMethods as LM
from Capstone_2.Pages.home import ValidationMethods as HM
from Capstone_2.Locators import locators as lc
from Capstone_2.Locators.locators import LoginLocators as LL




@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def class_inst(driver):
    logins = LM(driver)
    return logins

@pytest.fixture(scope='session')
def clas_inst(driver):
    logs = HM(driver)
    return logs


def test_TC_PIM_01(class_inst):
    url = lc.login_url
    class_inst.go_to_page(url)
    result = class_inst.forgot_password_link()
    assert result == 'Reset Password link sent successfully'


def test_TC_PIM_02(clas_inst):
    url = lc.login_url
    clas_inst.go_to_page(url)
    clas_inst.login_to_OragneHRM_stat(LL.valid_username,LL.valid_password)
    result_1 = clas_inst.title_verification()
    result_2 = clas_inst.validation_on_admin_page()
    assert result_1 == 'OrangeHRM'
    assert result_2 == lc.side_panel


def test_TC_PIM_03(clas_inst):
    result = clas_inst.validate_main_menu()
    assert result == lc.main_menu











